import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_query(query: str):
    vector = model.encode([query], convert_to_numpy=True)
    vector = vector.astype("float32")
    faiss.normalize_L2(vector)
    return vector


def semantic_search(query, index, chunks, top_k=3):
    query_vector = embed_query(query)
    scores, indices = index.search(query_vector, top_k)

    results = []
    for idx in indices[0]:
        if idx != -1:
            results.append(chunks[idx])

    return results
