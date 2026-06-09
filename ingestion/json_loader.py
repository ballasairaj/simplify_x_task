import json
from langchain.schema import Document

def load_json(path):

    with open(path) as f:
        logs = json.load(f)

    docs = []

    for item in logs:

        docs.append(
            Document(
                page_content=str(item),
                metadata={
                    "source": path,
                    "department": "security"
                }
            )
        )

    return docs