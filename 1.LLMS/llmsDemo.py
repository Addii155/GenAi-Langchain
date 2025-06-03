from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

ll = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

res = ll.invoke("What is the capital of India?")
print(res.content)