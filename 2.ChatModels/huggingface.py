from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)
model= ChatHuggingFace(
    llm=llm
)

res = model.invoke("What is the capital of France?")
print(res.content)
