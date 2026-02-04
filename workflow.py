from langgraph.graph import StateGraph
from pdf_loader import extract_snippets
from file_manager import save_pdf
from llm import classify_pdf

# Step 1: Load PDF
def load_pdf(state: dict) -> dict:
    text = extract_snippets(state["pdf_path"])
    return {**state, "text": text}

# Step 2: Save PDF
def save_file(state: dict) -> dict:
    save_pdf(
        state["pdf_path"],
        state["subject"],
        state["topic"]
    )
    return state

# Build graph
graph = StateGraph(dict)

graph.add_node("load_pdf", load_pdf)
graph.add_node("classify_pdf", classify_pdf)
graph.add_node("save_file", save_file)

graph.set_entry_point("load_pdf")
graph.add_edge("load_pdf", "classify_pdf")
graph.add_edge("classify_pdf", "save_file")

app = graph.compile()
