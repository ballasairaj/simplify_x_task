from langchain.vectorstores import Chroma

from langchain.embeddings import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory="vectorstore/chroma_db",
    embedding_function=embedding
)

def retrieve(query):

    return db.similarity_search(
        query,
        k=10
    )