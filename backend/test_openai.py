import os
from openai import OpenAI

print("ENV KEY PRESENT:", "OPENAI_API_KEY" in os.environ)

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"]
)

emb = client.embeddings.create(
    model="text-embedding-3-small",
    input="test"
)

print(emb.data[0].embedding[:5])
