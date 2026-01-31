from rag.pdf_to_text import pdf_to_text
from rag.chunker import chunk_text
from rag.embed_store import build_index, load_index
from rag.search import semantic_search

# Load & index data
text = pdf_to_text("data/sample.pdf")
chunks = chunk_text(text)

build_index(chunks, "data/index.faiss", "data/chunks.json")
index, stored_chunks = load_index("data/index.faiss", "data/chunks.json")

# Ask a question
query = "How much sales came from Swiggy?"

results = semantic_search(query, index, stored_chunks, top_k=2)

print("QUESTION:", query)
print("\nRETRIEVED CHUNKS:")
for r in results:
    print("\n---")
    print(r)
