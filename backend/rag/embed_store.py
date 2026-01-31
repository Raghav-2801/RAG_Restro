import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load local embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")
EMBED_DIM = 384  # fixed for this model


def build_index(chunks, index_path, meta_path):
    """
    Convert text chunks into embeddings and store them in FAISS
    """
    # Generate embeddings locally
    vectors = model.encode(chunks, convert_to_numpy=True)

    # FAISS requires float32
    vectors = vectors.astype("float32")

    # Normalize for cosine similarity
    faiss.normalize_L2(vectors)

    # Create FAISS index
    index = faiss.IndexFlatIP(EMBED_DIM)
    index.add(vectors)

    # Save index
    faiss.write_index(index, index_path)

    # Save original chunks
    with open(meta_path, "w") as f:
        json.dump({"chunks": chunks}, f)


def load_index(index_path, meta_path):
    """
    Load FAISS index and chunk metadata
    """
    index = faiss.read_index(index_path)

    with open(meta_path) as f:
        chunks = json.load(f)["chunks"]

    return index, chunks
