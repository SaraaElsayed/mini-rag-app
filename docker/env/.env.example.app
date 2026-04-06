APP_NAME="mini_RAG"
APP_VERSION="0.1"
OPENAI_API_KEY="skgji"

FILE_ALLOWED_TYPES=["text/plain","application/pdf"]
FILE_MAX_SIZE=10
FILE_DEFAULT_CHUNK_SIZE=512000 #KB



POSTGRES_USERNAME="postgres"
POSTGRES_PASSWORD=""
POSTGRES_HOST="localhost"
POSTGRES_PORT=5432
POSTGRES_MAIN_DATABASE="mini-rag"


# ========================= LLM Config =========================
GENERATION_BACKEND = "COHERE"
EMBEDDING_BACKEND = "COHERE"

OPENAI_API_KEY=""
OPENAI_API_URL=""
COHERE_API_KEY=""

GENERATION_MODEL_ID_LITERAL=["gpt-3.5-turbo-0125","command-a-03-2025"]
GENERATION_MODEL_ID="command-a-03-2025"
EMBEDDING_MODEL_ID_LITERAL=["embed-multilingual-light-v3.0","sentence-transformers/all-MiniLM-L6-v2"]
EMBEDDING_MODEL_ID="embed-multilingual-light-v3.0"
EMBEDDING_MODEL_SIZE=384

INPUT_DAFAULT_MAX_CHARACTERS=1024
GENERATION_DAFAULT_MAX_TOKENS=200
GENERATION_DAFAULT_TEMPERATURE=0.1

# ========================= Vector DB Config =========================
VECTOR_DB_BACKEND_LITERAL=["PGVECTOR","QDRANT"]
VECTOR_DB_BACKEND="PGVECTOR"
VECTOR_DB_PATH="qdrant_db"
VECTOR_DB_DISTANCE_METHOD="cosine"
VECTOR_DB_PGVEC_INDEX_THRESHOLD = 500

# ========================= Template Config ==========================
PRIMARY_LANG="ar"
DEFAULT_LANG="ar"