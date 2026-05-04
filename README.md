Multimodal RAG: Attention Is All You Need
This project implements a Multimodal Retrieval-Augmented Generation (RAG) system specifically designed to analyze the "Attention Is All You Need" research paper. By leveraging Cohere's embedding and LLM capabilities, the system can retrieve and reason over both text and visual elements (figures/tables) found within the document.

🚀 Key Features
Multimodal Processing: Extracts and describes images/figures from PDFs to provide visual context during retrieval.

Vector Search: Utilizes FAISS for efficient similarity searching of document embeddings.

Query Rewriting: Includes a specialized module to optimize user queries for better retrieval accuracy.

State-of-the-Art LLM: Powered by Cohere for high-quality text generation and semantic understanding.

📂 Project Structure
Plaintext
RAG PROJECT/
├── BACKEND/src/
│   ├── ingest.py           # Handles PDF processing and vector store creation
│   ├── llm_describer.py    # Generates descriptions for images/tables
│   ├── pdf_loader.py       # Extracts content from the source PDF
│   ├── query_rewriter.py   # Refines user prompts for better retrieval
│   ├── rag.py              # Core RAG logic and LLM orchestration
│   ├── retriever.py        # Logic for fetching relevant context from FAISS
│   └── main.py             # FastAPI entry point
├── DATA/
│   ├── faiss_store/        # Local vector database storage
│   └── pdfs/               # Source document: ATTENTION PAPPER.pdf
├── FRONTEND/               # User interface components
└── requirements.txt        # Project dependencies
🛠️ Tech Stack
LLM & Embeddings: Cohere

Vector Database: FAISS

Backend: FastAPI

PDF Processing: PyMuPDF / LangChain (for extraction)

Containerization: Docker

⚙️ Installation
Clone the repository:

Bash
git clone <your-repo-url>
cd "RAG PROJECT"
Set up a virtual environment:

Bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:

Bash
pip install -r requirements.txt
Configure Environment Variables:
Create a .env file based on .env.example:

Code snippet
COHERE_API_KEY=your_api_key_here
🚀 Usage
1. Data Ingestion
Process the "Attention Is All You Need" paper and populate the FAISS vector store:

Bash
python BACKEND/src/ingest.py
2. Run the Backend
Start the FastAPI server:

Bash
uvicorn BACKEND.src.main:app --reload
🧠 System Workflow
Ingestion: pdf_loader.py extracts text and images. llm_describer.py uses an LLM to "see" and describe the images.

Indexing: Both text and image descriptions are embedded via Cohere and stored in faiss_store.

Querying: A user query is rewritten for clarity by query_rewriter.py.

Retrieval: retriever.py finds the most relevant text and visual descriptions.

Generation: rag.py sends the combined context to the Cohere LLM to generate an informed response.