"""
Configuration file for RAG Restro.
Supports environment variables for easy deployment.
"""

import os
from pathlib import Path

# Debugging
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# Paths
BASE_DIR = Path(__file__).parent
DATA_DIR = os.getenv("DATA_DIR", str(BASE_DIR / "data"))
PDF_PATH = os.getenv("PDF_PATH", "data/BombayVadaPav.pdf")
INDEX_FILE = os.getenv("INDEX_FILE", os.path.join(DATA_DIR, "final.index"))
META_FILE = os.getenv("META_FILE", os.path.join(DATA_DIR, "final.json"))

# LLM Settings
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
LLM_MODEL = os.getenv("LLM_MODEL", "llama3.2:1b")

# Embedding Settings
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
EMBED_DIM = 384

# Search Settings
TOP_K = int(os.getenv("TOP_K", "2"))

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)
