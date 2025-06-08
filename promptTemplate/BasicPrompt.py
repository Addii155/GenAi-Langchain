from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

template=PromptTemplate(
    template="You are helping a user with their query: {query}.please provide a detailed response",
    input_variables=["query"]
)
prompt= template.format(query="Kubernetes working?")

model= ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
    temperature=0.2,
)
print(prompt)
res= model.invoke(prompt)
print(res.content)