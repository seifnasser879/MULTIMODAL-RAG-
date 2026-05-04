from langchain_cohere.chat_models import ChatCohere
from config import llm_temperature, COHEREAPI

llm =ChatCohere(cohere_api_key=COHEREAPI,temperature=llm_temperature)


def rewrite_query(query: str) -> str:

    prompt = f"""
You are a query rewriting assistant for document retrieval systems.

Goal:
Rewrite the user message into a concise, search-optimized query that reflects its technical or domain-specific intent.

Rules:
- If the message is conversational, personal, ambiguous, or not answerable from documents, return it EXACTLY as is.
- Rewrite ONLY if it improves retrieval quality.
- Preserve the original meaning and domain (e.g., AI, ML, databases, math, software engineering).
- Do NOT add new concepts, assumptions, or keywords.
- Remove filler words, greetings, and unnecessary phrasing.
- Prefer precise technical terms implied by the user.
- Output ONE short, standalone query.
- Output ONLY the rewritten query (no explanations, quotes, or additional text).

User message:
{query}

Rewritten search query:
"""
    return llm.invoke(prompt).content.strip()




