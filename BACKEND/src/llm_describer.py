import fitz  # PyMuPDF
from langchain_cohere.chat_models import ChatCohere
from langchain_core.messages import HumanMessage
from config import COHEREAPI, llm_temperature , llm



def describe_with_llm(content: str, content_type: str, hint: str = None) -> str:
    """Sends extracted data to Cohere for cleaning or summarization."""
    if not content or len(content.strip()) < 5:
        return ""

    if content_type == "table":
        instruction = "Summarize this table's structure and extract key insights."
    elif content_type == "image":
        instruction = "This text was extracted from an image area. Describe the likely content and insights."
    else:
        instruction = "Clean and summarize this text for a RAG system. Remove headers, footers, and noise."

    hint_text = f" [{hint}]" if hint else ""
    prompt = f"You are a data analyst.\n\n{instruction}{hint_text}\n\nContent:\n{content}"
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content.strip()
    