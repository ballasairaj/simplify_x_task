from langchain_community.document_loaders import PyPDFLoader

def load_pdf(path):

    loader = PyPDFLoader(path)

    docs = loader.load()

    for doc in docs:
        doc.metadata.update({
            "source": path,
            "department": "finance"
        })

    return docs