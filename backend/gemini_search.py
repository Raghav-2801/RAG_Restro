# test_search.py
from rag.embed_store import load_index
from rag.search import semantic_search

# 1. Define Paths (Must match what you used in Step 4)
INDEX_FILE = "data/my_cafe.index"
META_FILE = "data/my_cafe.json"

# 2. Load the Brain (Eating the meal you cooked)
print("Loading database...")
index, stored_chunks = load_index(INDEX_FILE, META_FILE)

# 3. Define a Query
query = "What is the total sales?" 
# (Try changing this to "How much from Zomato?" later)

print(f"\nSearching for: '{query}'")

# 4. Search
results = semantic_search(query, index, stored_chunks, top_k=1)

# 5. Print Results
print("\n--- BEST MATCH ---")
if results:
    print(results[0])
else:
    print("No results found.")