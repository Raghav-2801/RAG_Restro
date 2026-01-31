from rag.pdf_to_text import pdf_to_text
from rag.chunker import chunk_text
from rag.embed_store import build_index, load_index

text = pdf_to_text("data/30th-jan-26.pdf")
chunks = chunk_text(text)

build_index(
    chunks,
    "data/index.faiss",
    "data/chunks.json"
)

index, stored_chunks = load_index(
    "data/index.faiss",
    "data/chunks.json"
)

print("Chunks stored:", len(stored_chunks))
print("FAISS index size:", index.ntotal)
