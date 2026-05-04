
from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from config import embedding, INDEX_DIR
from langchain_community.retrievers import BM25Retriever
import os

def create_embedding(text_list: List[str]):

    if not text_list:
        raise ValueError("text_list cannot be empty")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=812,
        chunk_overlap=150,
        separators=["\n\n", "\n", ". ", " ", ""],
    )

    documents = []

    for item in text_list:
        if not item:
            continue

        # Strip the tags used during the description phase
        if item.startswith("[TABLE SUMMARY]:"):
            content = item.replace("[TABLE SUMMARY]:", "").strip()
        elif item.startswith("[IMAGE SUMMARY]:"):
            content = item.replace("[IMAGE SUMMARY]:", "").strip()
        else:
            content = item.strip()

        # Filtering noise
        if len(content) < 30:
            continue
        if "\\" in content and ":" in content:
            continue

        chunks = splitter.split_text(content)

        for chunk in chunks:
            # Metadata is removed here
            documents.append(Document(page_content=chunk))

    if not documents:
        raise ValueError("No valid documents generated after processing.")

    # Create and Save
    vectorstore = FAISS.from_documents(documents, embedding)
    bm25_retriever = BM25Retriever.from_documents(documents)
    bm25_retriever.k = 4
    if not os.path.exists(INDEX_DIR):
        os.makedirs(INDEX_DIR)
        
    vectorstore.save_local(INDEX_DIR)

    return vectorstore, documents

