from rag.pdf_to_text import pdf_to_text
from rag.chunker import chunk_text
from rag.embed_store import build_index, load_index
from rag.search import semantic_search
from rag.answer import generate_answer

# Build index
text = pdf_to_text("data/sample.pdf")
chunks = chunk_text(text)
build_index(chunks, "data/index.faiss", "data/chunks.json")

index, stored_chunks = load_index("data/index.faiss", "data/chunks.json")

# Ask question
question = "How much sales came from Swiggy?"

retrieved = semantic_search(question, index, stored_chunks, top_k=2)
answer = generate_answer(question, retrieved)

print("QUESTION:")
print(question)
print("\nANSWER:")
print(answer)
