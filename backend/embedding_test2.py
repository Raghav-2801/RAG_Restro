import os
from rag.pdf_to_text import pdf_to_text
from rag.chunker import chunk_text
from rag.embed_store import build_index, load_index

# 1. Define where we want to save our files
# (Think of these as the filenames you choose in "Save As")
INDEX_FILE = "data/my_cafe.index"
META_FILE = "data/my_cafe.json"

# 2. Get the Raw Data
print("--- STEP 1: Processing PDF ---")
raw_text = pdf_to_text("data/30th-jan-26.pdf")
chunks = chunk_text(raw_text)
print(f"Generated {len(chunks)} text chunks.")

# 3. Build & Save (The "Cooking" Phase)
print("\n--- STEP 2: Building Index (Cooking) ---")
build_index(chunks, INDEX_FILE, META_FILE)
print("Index built and saved to disk!")

# 4. Load (The "Eating" Phase)
# We overwrite the variables to prove we are loading fresh from disk
print("\n--- STEP 3: Loading Index (Eating) ---")
loaded_index, loaded_chunks = load_index(INDEX_FILE, META_FILE)

# 5. Verification
print(f"Loaded Index contains {loaded_index.ntotal} vectors.")
print(f"Loaded Metadata contains {len(loaded_chunks)} text chunks.")

if loaded_index.ntotal == len(loaded_chunks):
    print("\nSUCCESS: Math and Text are perfectly synced!")
else:
    print("\nERROR: Mismatch between vectors and text.")