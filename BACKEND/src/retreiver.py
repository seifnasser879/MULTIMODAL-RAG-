from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_cohere.embeddings import CohereEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from config import INDEX_DIR, COHEREAPI, embedding




def get_retriever_from_loaded_docs(index_path: str):
    stored = FAISS.load_local(
        index_path,
        embedding,
        allow_dangerous_deserialization=True
    )

    retriever = stored.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 4,
            "fetch_k": 20
        }
    )

    return retriever