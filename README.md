# 🧠 Mini RAG Application — Production-Ready Q&A System

A production-ready **Retrieval-Augmented Generation (RAG)** system that allows users to upload documents, organize them into topic-based projects, and query them through a RESTful API to get accurate, context-aware answers powered by LLMs.

---

## 🎥 Demo

> 📹 [Watch the demo video](https://youtu.be/UC2eYflcIbc)

---

## ✨ Features

- 📁 **Multi-Project Document Management** — organize uploaded documents into isolated projects by topic (e.g. Health, Business, Legal)
- 🔍 **Semantic Search** — retrieve the most relevant chunks using vector similarity search
- 🤖 **LLM-Powered Answers** — generate accurate, context-aware responses using Cohere LLMs
- 🧩 **Dual Vector Store Support** — works with both Qdrant and PGVector (PostgreSQL)
- 🏗️ **Clean MVC Architecture** — well-structured codebase across controllers, models, routes, and helpers
- 🐳 **Fully Containerized** — Docker & Docker Compose with Nginx as reverse proxy
- 📊 **Observability Stack** — real-time monitoring with Prometheus & Grafana

---

## 🏛️ Architecture

```bash
User Request
│
▼
Nginx (Reverse Proxy)
│
▼
FastAPI Backend
│
├── Routes (data / nlp / base)
│
├── Controllers
│   ├── ProjectController   → manage projects
│   ├── DataController      → handle document uploads
│   ├── NLPController       → RAG pipeline logic
│   └── ProcessController   → chunking & embedding
│
├── Models
│   ├── ProjectModel
│   ├── AssetModel
│   └── ChunkModel
│
└── Stores
├── PGVector (PostgreSQL)
└── Qdrant
```
---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI, Python 3.8+ |
| RAG Pipeline | LangChain |
| Embeddings & LLM | Cohere |
| Vector Store | Qdrant / PGVector (PostgreSQL) |
| Containerization | Docker, Docker Compose |
| Reverse Proxy | Nginx |
| Monitoring | Prometheus, Grafana |
| API Testing | Postman |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or later
- Docker & Docker Compose
- Cohere API Key

### 1. Clone the Repository

```bash
git clone https://github.com/SaraaElsayed/mini-rag-app.git
cd mini-rag-app
```

### 2. Install System Dependencies

```bash
sudo apt update
sudo apt install libpq-dev gcc python3-dev
```

### 3. Set Up Python Environment (via MiniConda)

```bash
conda create -n mini-rag python=3.8
conda activate mini-rag
```

### 4. Install Python Packages

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

```bash
cp .env.example .env
```

Edit `.env` and fill in your credentials


---

## ▶️ Running the App

### Option A — Local (FastAPI Dev Server)

```bash
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

### Option B — Docker Compose (Recommended)

```bash
cd docker
cp .env.example .env
# update .env with your credentials
sudo docker compose up -d
```

This starts all services: FastAPI, PostgreSQL, Qdrant, Nginx, Prometheus, and Grafana.

---

## 📬 API Overview

Download the full Postman collection: [`/assets/mini-rag-app.postman_collection.json`](/assets/mini-rag-app.postman_collection.json)

| Method | Endpoint | Description |
|---|---|---|
| GET  | `/welcome-request` | Health check — verify the server is running |
| POST | `/upload` | Upload a document and assign it to a project (creates project if it doesn't exist) |
| POST | `/process` | Process a specific file by `file_id` — chunk and prepare for embedding |
| POST | `/nlp_index_push` | Push processed chunks into the vector store |
| GET  | `/nlp_index_info` | Get info about a pushed file (e.g. number of chunks stored) |
| POST | `/nlp_index_search` | Search the vector store and retrieve the most relevant document chunks |
| POST | `/nlp_index_answer` | Query the project — retrieves context and returns an LLM-generated answer |

---

## 📁 Project Structure

```bash
mini-rag-app/
├── docker/                  # Docker & Compose configuration
├── src/
│   ├── assets/              # Static assets & Postman collection
│   ├── controllers/         # Business logic layer
│   │   ├── BaseController.py
│   │   ├── DataController.py
│   │   ├── NLPController.py
│   │   ├── ProcessController.py
│   │   └── ProjectController.py
│   ├── helpers/             # Config & utility functions
│   ├── models/              # Data models & DB schemas
│   │   ├── AssetModel.py
│   │   ├── BaseDataModel.py
│   │   ├── ChunkModel.py
│   │   └── ProjectModel.py
│   ├── routes/              # API route definitions
│   │   ├── base.py
│   │   ├── data.py
│   │   └── nlp.py
│   ├── stores/              # Vector store integrations
│   ├── utils/               # Helper utilities
│   └── main.py              # App entry point
├── requirements.txt
├── .env.example
└── README.md
```
---


