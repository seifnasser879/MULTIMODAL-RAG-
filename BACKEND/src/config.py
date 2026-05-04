import os
from dotenv import load_dotenv
from langchain_cohere.embeddings import CohereEmbeddings
from langchain_cohere.chat_models import ChatCohere
BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

load_dotenv()

DATA_DIR = os.path.join(BASE_DIR, "DATA","RAG_cheatsheet.pdf")
INDEX_DIR = os.path.join(BASE_DIR, "DATA", "faiss_store")
pdf_data = os.path.join(BASE_DIR,"DATA","pdfs","ATTENTION PAPPER.pdf")
IMAGE_OUTPUT_DIR=os.path.join(BASE_DIR,"DATA","images")
COHEREAPI = os.getenv("cohere")
gemeni_api= os.getenv("gemini")
cohere_embedding_model="embed-english-v3.0"
gemini_embedding_model="gemini-embedding-2-preview"
cohere_reranker="rerank-english-v3.0"
llm_temperature=0.2
embedding = CohereEmbeddings(
    model="embed-english-light-v3.0",
    cohere_api_key=COHEREAPI
)

llm=ChatCohere(
    cohere_api_key=COHEREAPI,
    temperature=llm_temperature
)

print(BASE_DIR)
