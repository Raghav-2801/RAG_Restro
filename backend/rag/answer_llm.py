import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:1b"


def generate_answer_llm(question, retrieved_chunks):
    if not retrieved_chunks:
        return "Sorry, no relevant data found."

    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
    You are a helpful assistant. Answer the question based ONLY on the text below.
    
    TEXT DATA:
    {context}
    
    QUESTION:
    {question}
    
    ANSWER:
    """

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=60
    )

    response.raise_for_status()
    return response.json()["response"].strip()
