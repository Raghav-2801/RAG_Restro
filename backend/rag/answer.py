def generate_answer(question, retrieved_chunks):
    """
    Simple answer generator using retrieved text
    """
    if not retrieved_chunks:
        return "Sorry, I could not find relevant data."

    answer = "Based on the restaurant data:\n\n"

    for chunk in retrieved_chunks:
        answer += chunk.strip() + "\n\n"

    return answer.strip()
