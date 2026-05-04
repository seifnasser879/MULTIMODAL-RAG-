import os
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

from pdf_loader import process_pdf
from retreiver import get_retriever_from_loaded_docs
from ingest import create_embedding
from config import INDEX_DIR, pdf_data, llm


if not os.path.exists(INDEX_DIR):
    print("Index not found. Starting PDF processing and embedding...")

    texts = process_pdf(pdf_data)
    vectorstore=create_embedding(texts)



retriever = get_retriever_from_loaded_docs(INDEX_DIR)



memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)




qa_prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a helpful assistant.

IMPORTANT:
- Always answer in English only
- Use the context ONLY if it is useful
- Ignore irrelevant context
- Answer clearly and naturally
- Remember previous conversation when helpful

Context:
{context}

Question:
{question}

Answer:
"""
)



chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory,
    combine_docs_chain_kwargs={
        "prompt": qa_prompt
    },
    return_source_documents=False,
)



def get_answer(query: str):
    result = chain.invoke({
        "question": query
    })

    return result["answer"]