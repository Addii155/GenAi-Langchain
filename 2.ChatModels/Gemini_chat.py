from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict
import os
from dotenv import load_dotenv
load_dotenv()

model=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2,
    api_key=os.getenv("GOOGLE_API_KEY"),
)

class structure_provider(TypedDict):
    summary: str
    sentiment: str

sturcture_model=model.with_structured_output(structure_provider)


res=sturcture_model.invoke("wi")
print(res.content)