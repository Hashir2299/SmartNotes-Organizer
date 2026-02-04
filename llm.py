import os
from langchain_ollama import ChatOllama
from config import SUBJECTS

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "deepseek-r1:8b")

llm = ChatOllama(
    model=OLLAMA_MODEL,
    temperature=0
)

def classify_pdf(state: dict) -> dict:
    prompt = f"""
You are organizing study PDFs.

Allowed subjects (you MUST choose one):
{SUBJECTS}

Rules:
- Choose exactly ONE subject from the list
- Generate a short topic name (2–5 words)
- Never say unknown or uncertain
Tips:
- Anything related to C++ goes under Programming Fundamentals C++,if it does not contain code then choose other subjects
- Calculus contains topics like limits, derivatives, integrals,etc
- Discrete Mathematics includes combinatorics, series, arithmetic, graph theory, logic, add/or tables related things, set theory, etc
- Applications of Information & Communication Technology includes networking, databases, web technologies, viruses, security and internet, etc
- Applied Physics and Calculus can be in handwritten form

PDF content:
{state["text"][:2000]}

Respond exactly in this format:
Subject: <subject>
Topic: <topic>
"""

    response = llm.invoke(prompt).content.strip()

    subject = response.split("Subject:")[1].split("\n")[0].strip()
    topic = response.split("Topic:")[1].strip()

    return {
        **state,
        "subject": subject,
        "topic": topic
    }
