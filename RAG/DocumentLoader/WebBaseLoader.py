from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv
load_dotenv()
import os
os.environ["USER_AGENT"] = os.getenv("USER_AGENT", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
loader= WebBaseLoader("https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/408")

doc= loader.load()

print(doc)