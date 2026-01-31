from rag.pdf_to_text import pdf_to_text
from rag.chunker import chunk_text

text = pdf_to_text("data/30th-jan-26.pdf")
chunks = chunk_text(text, max_tokens=45, overlap=10)

print("Total chunks:", len(chunks))

for i, c in enumerate(chunks):
    print(f"\n--- CHUNK {i+1} ---")
    print(c)