from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader("RAG/DocumentLoader/aditya.pdf")

docs=loader.load();

print(docs)

# pypdfLoader ->text but not work in scanned images pdf

# for table -> PDFPlumberLoader
# sacnner -> UnstructurePdfLoader