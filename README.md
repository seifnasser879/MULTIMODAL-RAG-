# 📚 Multimodal RAG: Attention Is All You Need

A Multimodal Retrieval-Augmented Generation (RAG) system that intelligently analyzes the **"Attention Is All You Need"** research paper. This system extracts and indexes both text and visual elements (figures, tables, diagrams), enabling sophisticated semantic search and knowledge generation powered by Cohere.

## 🚀 Key Features

- **🖼️ Multimodal Processing** - Extracts and generates descriptions for images, figures, and tables from PDFs, preserving visual context in retrieval
- **⚡ Vector Search** - Efficient similarity search using FAISS vector database for fast, accurate document retrieval
- **🔄 Query Optimization** - Intelligent query rewriting module to refine user prompts and improve retrieval accuracy
- **🧠 Advanced LLM Integration** - Powered by Cohere for semantic understanding and high-quality text generation
- **🌐 REST API** - FastAPI-based backend for easy integration with frontend applications

## 📂 Project Structure

```
RAG PROJECT/
├── BACKEND/src/
│   ├── config.py           # Configuration and environment setup
│   ├── ingest.py           # PDF processing & vector store initialization
│   ├── llm_describer.py    # AI-powered image/table description generation
│   ├── pdf_loader.py       # PDF extraction (text & images)
│   ├── query_rewriter.py   # Query optimization for better retrieval
│   ├── rag.py              # Core RAG orchestration logic
│   ├── retreiver.py        # FAISS-based context retrieval
│   ├── main.py             # FastAPI application entry point
│   └── __init__.py
├── DATA/
│   ├── faiss_store/        # Vector database storage (auto-generated)
│   └── pdfs/               # Source documents (e.g., ATTENTION_PAPER.pdf)
├── FRONTEND/
│   └── frontend.html       # Web UI for querying the RAG system
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variables template
└── README.md              # This file
```

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **LLM & Embeddings** | Cohere |
| **Vector Database** | FAISS (CPU) |
| **Backend Framework** | FastAPI |
| **API Server** | Uvicorn |
| **PDF Processing** | LangChain, PyMuPDF |
| **Environment Management** | python-dotenv |

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Cohere API key (get it from [cohere.ai](https://cohere.ai))

### Step 1: Clone the Repository

```bash
git clone <your-repo-url>
cd "RAG PROJECT"
```

### Step 2: Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit `.env` and add your Cohere API key:

```env
COHERE_API_KEY=your_cohere_api_key_here
```

## 🚀 Quick Start

### 1. Ingest Document Data

Process the PDF and create the vector store:

```bash
python BACKEND/src/ingest.py
```

This will:
- Extract text and images from the PDF
- Generate AI descriptions for visual elements
- Create embeddings using Cohere
- Build and save the FAISS vector index

### 2. Start the Backend Server

```bash
uvicorn BACKEND.src.main:app --reload
```

The API will be available at `http://localhost:8000`

- **API Documentation**: `http://localhost:8000/docs` (Swagger UI)
- **Alternative Docs**: `http://localhost:8000/redoc` (ReDoc)

### 3. Access the Frontend

Open `FRONTEND/frontend.html` in your web browser to interact with the RAG system.

## 🧠 System Architecture

### Data Flow

```
PDF Input
    ↓
[PDF Loader] - Extracts text & images
    ↓
[LLM Describer] - Generates descriptions for visual elements
    ↓
[Cohere Embeddings] - Converts text to vectors
    ↓
[FAISS Index] - Stores vectors for fast retrieval
    ├─────────────────────────────────┐
    ↓                                 ↓
[Query Input]                   [Vector Store]
    ↓                                 ↓
[Query Rewriter] - Optimizes query
    ↓
[Cohere Embeddings] - Vectorizes optimized query
    ↓
[Retriever] - Finds top-k similar vectors
    ↓
[RAG] - Combines context + query
    ↓
[Cohere LLM] - Generates informed response
    ↓
[Response Output]
```

### Component Details

| Module | Purpose |
|--------|---------|
| **pdf_loader.py** | Extracts text content and images from PDF files |
| **llm_describer.py** | Uses Cohere LLM to generate descriptive text for images/figures |
| **ingest.py** | Orchestrates PDF processing, embedding, and FAISS index creation |
| **query_rewriter.py** | Refines user queries to improve retrieval accuracy |
| **retriever.py** | Queries FAISS index and returns top-k relevant documents |
| **rag.py** | Combines retrieved context with user query for LLM generation |
| **main.py** | Exposes REST API endpoints for frontend communication |
| **config.py** | Manages configuration and environment variables |

## 📡 API Endpoints

### Query Endpoint

```bash
POST /query
Content-Type: application/json

{
  "query": "What is the attention mechanism?"
}
```

**Response:**
```json
{
  "response": "The attention mechanism is a neural network technique that...",
  "sources": [
    {
      "type": "text",
      "content": "..."
    },
    {
      "type": "image_description",
      "content": "..."
    }
  ]
}
```

## 🔧 Development

### Running Tests
```bash
# Run the backend tests (if available)
pytest BACKEND/src/
```

### Enable Debug Mode
Update the `.env` file:
```env
DEBUG=true
```

## 📝 Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `COHERE_API_KEY` | Cohere API authentication key | `abc123xyz...` |
| `FAISS_INDEX_PATH` | Path to FAISS vector store | `DATA/faiss_store/` |
| `PDF_PATH` | Path to source PDF file | `DATA/pdfs/` |
| `DEBUG` | Enable debug logging | `false` |

## 🐛 Troubleshooting

### Issue: "COHERE_API_KEY not found"
- **Solution**: Ensure `.env` file exists in the project root with your Cohere API key

### Issue: "FAISS index not found"
- **Solution**: Run `python BACKEND/src/ingest.py` to create the vector index

### Issue: Slow query performance
- **Solution**: Check FAISS index size and consider rebuilding with larger k-value

## 📚 References

- [Attention Is All You Need Paper](https://arxiv.org/abs/1706.03762)
- [Cohere Documentation](https://docs.cohere.ai)
- [FAISS Documentation](https://github.com/facebookresearch/faiss)
- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [LangChain Documentation](https://python.langchain.com)


