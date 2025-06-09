from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2,
    api_key=os.getenv("GOOGLE_API_KEY"),
)

prompts = PromptTemplate(
    template="Give five interesting facts about {topic}.",
    input_variables=["topic"]
)

parser = StrOutputParser()

chain = prompts | model | parser

res = chain.invoke({"topic": "Python programming language"})
print(res)

chain.get_graph().print_ascii()
