from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence
import os
load_dotenv()

prompts=PromptTemplate(
    template='Write a joke on {topic}',
    input_variables=['topic']
)

model=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2,
    api_key=os.getenv("GOOGLE_API_KEY"),
)

parser=StrOutputParser()

chain=RunnableSequence(prompts,model,parser)

print(chain.invoke({"topic":"AI"}))