from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence ,RunnableParallel
from langchain_core.prompts import PromptTemplate
import os
load_dotenv()

prompt1=PromptTemplate(
    template='Write a Linkedin post on the {topic}',
    input_variables=['topic']
)
prompt1=PromptTemplate(
    template='Write a twitter post on the {topic}',
    input_variables=['topic']
)

model=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2,
    api_key=os.getenv("GOOGLE_API_KEY"),
)

parser=StrOutputParser()

result= RunnableParallel({
    "twitter":RunnableSequence(prompt1,model,parser),
    "linkedin":RunnableSequence(prompt1,model,parser)
}
)

res=result.invoke({"topic":"JWT"})

print(res["twitter"])
print(res["linkedin"])