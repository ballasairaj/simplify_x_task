import pandas as pd
from langchain.schema import Document

def load_csv(path):

    df = pd.read_csv(path)

    docs = []

    for _, row in df.iterrows():

        docs.append(
            Document(
                page_content=str(row.to_dict()),
                metadata={
                    "source": path,
                    "department": "reports"
                }
            )
        )

    return docs