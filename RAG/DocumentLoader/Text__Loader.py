from langchain_community.document_loaders import TextLoader

import os
loader= TextLoader('Cricket.txt',encoding="utf-8")

# Print the current working directory
# print()

doc= loader.load()

print(doc)