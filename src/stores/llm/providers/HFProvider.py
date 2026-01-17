from ..LLMInterface import LLMInterface
from ..LLMEnums import HuggingFaceEnums
from huggingface_hub import InferenceClient
from sentence_transformers import SentenceTransformer
import logging

class HuggingFaceProvider(LLMInterface):

    def __init__(self, api_key: str,
                       default_input_max_characters: int=1000,
                       default_generation_max_output_tokens: int=1000,
                       default_generation_temperature: float=0.1):
        
        self.api_key = api_key

        self.default_input_max_characters = default_input_max_characters
        self.default_generation_max_output_tokens = default_generation_max_output_tokens
        self.default_generation_temperature = default_generation_temperature

        self.generation_model_id = None

        self.embedding_model_id = None
        self.embedding_size = None

        self.client = InferenceClient(
            token=self.api_key
            )

        self.enums = HuggingFaceEnums
        self.logger = logging.getLogger(__name__)

    def set_generation_model(self, model_id: str):
        self.generation_model_id = model_id

    def set_embedding_model(self, model_id: str, embedding_size: int):
        self.embedding_model_id = model_id
        self.embedding_size = embedding_size

        try:
            self.embedding_model = SentenceTransformer(model_id)
            self.logger.info(f"Loaded embedding model: {model_id}")
        except ImportError:
            self.logger.error("sentence-transformers not installed. Please run: pip install sentence-transformers")
        except Exception as e:
            self.logger.error(f"Failed to load embedding model: {str(e)}")

    def process_text(self, text: str):
        return text[:self.default_input_max_characters].strip()

    def generate_text(self, prompt: str, chat_history: list=[], max_output_tokens: int=None,
                            temperature: float = None):
        
        if not self.client:
            self.logger.error("HuggingFace client was not set")
            return None

        if not self.generation_model_id:
            self.logger.error("Generation model for HuggingFace was not set")
            return None
        
        max_output_tokens = max_output_tokens if max_output_tokens else self.default_generation_max_output_tokens
        temperature = temperature if temperature else self.default_generation_temperature

        chat_history.append(
            self.construct_prompt(prompt=prompt, role=HuggingFaceEnums.USER.value)
        )

        try:
            response = self.client.chat_completion(
                model=self.generation_model_id,
                messages=chat_history,
                max_tokens=max_output_tokens,
                temperature=temperature
            )

            if not response or not response.choices or len(response.choices) == 0 or not response.choices[0].message:
                self.logger.error("Error while generating text with HuggingFace")
                return None

            return response.choices[0].message.content

        except Exception as e:
            self.logger.error(f"Error while generating text with HuggingFace: {str(e)}")
            return None


    def embed_text(self, text: str, document_type: str = None):
        
        if not self.embedding_model:
            self.logger.error("Embedding model not loaded")
            return None
        
        try:
            embeddings = self.embedding_model.encode(text)
            return embeddings.tolist()
        except Exception as e:
            self.logger.error(f"Embedding failed: {str(e)}")
            return None

    def construct_prompt(self, prompt: str, role: str):
        return {
            "role": role,
            "content": self.process_text(prompt)
        }