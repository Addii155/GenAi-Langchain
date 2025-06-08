from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel , Field
from typing import List
from pdfminer.high_level import extract_text
from dotenv import load_dotenv
load_dotenv()
import os

print(os.getenv("GOOGLE_API_KEY"))
def extract_text_from_pdf(file_path: str) -> str:
    return extract_text(file_path)


class StructureProvider(BaseModel):
    Name: str = Field(description="Name of the person")
    Email: str = Field(description="Email address of the person")
    Skills: list[str] = Field(description="Skill provided in resume")
    Projects: list[str] = Field(description="Projects provided in resume")
    Education: list[str] = Field(description="Education provided in resume")
    Experience: list[str] = Field(description="Experience provided in resume")
    ATS_Score: int = Field(description="ATS score of the resume",gt=0 , lt=100)


model=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2,
    api_key=os.getenv("GOOGLE_API_KEY"),
)

# extract text from a pdf file 
pdf_text= extract_text_from_pdf(r"C:\Users\HP\OneDrive\Desktop\GenAi\Langchain_Models/structure_output/sample.pdf")
# print(pdf_text)
structure_model = model.with_structured_output(StructureProvider)
res=structure_model.invoke(pdf_text)
print(res)