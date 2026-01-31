# main.py
from config import DEBUG, PDF_PATH, INDEX_FILE, META_FILE, TOP_K
from rag.pdf_to_text import pdf_to_text
from rag.chunker import chunk_text
from rag.embed_store import build_index, load_index
from rag.search import semantic_search
from rag.answer_llm import generate_answer_llm

def run_app():
    # 1. CHECK: Does the database exist? If not, build it.
    print("--- 1. Checking Database ---")
    try:
        index, stored_chunks = load_index(INDEX_FILE, META_FILE)
        print("   Database loaded successfully.")
    except:
        print("   Database not found. Building from scratch...")
        text = pdf_to_text(PDF_PATH)
        chunks = chunk_text(text)
        build_index(chunks, INDEX_FILE, META_FILE)
        index, stored_chunks = load_index(INDEX_FILE, META_FILE)
        print("   Database built and loaded.")

    # 2. INPUT: Ask the user
    print("\n--- 2. Ready for Questions ---")
    question = input("Enter your question: ")

    # 3. SEARCH (The Librarian)
    print("\n--- 3. Searching... ---")
    retrieved = semantic_search(question, index, stored_chunks, top_k=TOP_K)
    
    # Debug output (only if DEBUG=True)
    if DEBUG:
        print("\n[DEBUG] The Librarian found this text:")
        for chunk in retrieved:
            print(f"---\n{chunk}\n---")
    
    print(f"   (Found {len(retrieved)} relevant chunks)")

    # 4. GENERATE (The Mouth)
    print("\n--- 4. Thinking... ---")
    final_answer = generate_answer_llm(question, retrieved)

    # 5. OUTPUT
    print("\n================ ANSWER ================")
    print(final_answer)
    print("========================================")

if __name__ == "__main__":
    run_app()