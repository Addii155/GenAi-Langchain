from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
import os
load_dotenv()
print(os.getenv("HUGGINGFACEHUB_API_KEY"))
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
    # huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_KEY")
)

chat = ChatHuggingFace(llm=llm)

print(chat.invoke("What is the capital of France?"))