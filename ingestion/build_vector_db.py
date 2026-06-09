from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

from ingestion.pdf_loader import load_pdf
from ingestion.csv_loader import load_csv
from ingestion.json_loader import load_json

import os

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

docs = []

for file in os.listdir("data/pdfs"):
    docs.extend(load_pdf(f"data/pdfs/{file}"))

for file in os.listdir("data/csvs"):
    docs.extend(load_csv(f"data/csvs/{file}"))

for file in os.listdir("data/logs"):
    docs.extend(load_json(f"data/logs/{file}"))

db = Chroma.from_documents(
    documents=docs,
    embedding=embedding,
    persist_directory="vectorstore/chroma_db"
)

print("Vector DB Created Successfully!")