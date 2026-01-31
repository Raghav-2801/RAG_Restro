import os
import json
import numpy as np
import faiss
from openai import OpenAI
from rag.pdf_to_text import pdf_to_text
from rag.chunker import chunk_text

# 1. Setup OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
from openai import OpenAI

# 2. Define the Indexing Function (The "Librarian")
def build_index(chunks):
    print("Converting chunks to numbers (Vectors)... this might take a moment.")
    
    vectors = []
    # Send each chunk to OpenAI to get the "Barcode"
    for i, chunk in enumerate(chunks):
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=chunk
        )
        vectors.append(response.data[0].embedding)
        print(f" - Processed chunk {i+1}/{len(chunks)}")

    # Convert list to a Math Array (FAISS format)
    vectors = np.array(vectors, dtype="float32")
    
    # Normalize (The "Math Trick" to make searching faster)
    faiss.normalize_L2(vectors)

    # Build the FAISS Machine
    dimension = vectors.shape[1] # 1536 dimensions
    index = faiss.IndexFlatIP(dimension)
    index.add(vectors)
    
    return index

# --- MAIN EXECUTION ---

# 1. Get Text
print("Reading PDF...")
raw_text = pdf_to_text("data/sample.pdf")

# 2. Chunk Text (Production Settings)
print("Chunking Text...")
chunks = chunk_text(raw_text, max_tokens=500, overlap=50)
print(f"Created {len(chunks)} chunks.")

# 3. Build Index
index = build_index(chunks)

# 4. Save the Files (The "Brain" and the "Notebook")
print("Saving files...")
faiss.write_index(index, "sales.index")

with open("sales_meta.json", "w") as f:
    json.dump({"chunks": chunks}, f)

print("\nSUCCESS! Database built.")
print("1. 'sales.index' (The Math)")
print("2. 'sales_meta.json' (The Text)")
