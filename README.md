# Enterprise RAG Assistant

An enterprise-grade Retrieval-Augmented Generation (RAG) system capable of retrieving information from multiple enterprise data sources while enforcing strict Role-Based Access Control (RBAC).

The system intelligently retrieves context from PDFs, CSV files, and JSON logs, then generates grounded answers using Mistral Large with source attribution and confidence scoring.

---

## Features

### Multi-Source Data Ingestion

Supports:

* PDF Documents
* CSV Files
* JSON Logs
* Enterprise Reports
* Structured Records

### Intelligent Retrieval

* Semantic Search
* Vector Search using ChromaDB
* Query-Aware Retrieval
* Cross-Source Context Aggregation

### Secure Access Control

* Role-Based Access Control (RBAC)
* Department-Level Permissions
* Restricted Document Access
* Sensitive Data Protection

### Answer Generation

* Mistral Large LLM
* Context-Grounded Responses
* Reduced Hallucinations
* Source Citations

### Explainability

* Confidence Score
* Retrieval Traceability
* Source Attribution

---

## Architecture

```text
                        User Query
                              |
                              v
                  +----------------------+
                  | Query Understanding |
                  +----------------------+
                              |
                              v
                  +----------------------+
                  | RBAC Permission Check|
                  +----------------------+
                              |
                              v
      +------------------------------------------------+
      |                Retrieval Layer                 |
      +------------------------------------------------+
             |              |                |
             v              v                v
          PDFs           CSV Files       JSON Logs
             \              |                /
              \             |               /
               +--------------------------+
               |      Chroma Vector DB    |
               +--------------------------+
                              |
                              v
                   Context Aggregation
                              |
                              v
                      Mistral Large
                              |
                              v
                  Answer + Citations +
                    Confidence Score
```

---

## Tech Stack

### Backend

* Python 3.11
* LangChain
* Mistral Large

### Vector Database

* ChromaDB

### Embeddings

* Sentence Transformers
* all-MiniLM-L6-v2

### Frontend

* Streamlit

### Data Processing

* Pandas
* PyPDF

### Retrieval

* Semantic Search
* Hybrid Search (Optional BM25)

---

## Project Structure

```text
enterprise-rag/
│
├── app.py
├── requirements.txt
├── .env
│
├── data/
│   ├── pdfs/
│   ├── csvs/
│   └── logs/
│
├── policies/
│   ├── roles.json
│   └── users.json
│
├── ingestion/
│   ├── __init__.py
│   ├── pdf_loader.py
│   ├── csv_loader.py
│   ├── json_loader.py
│   └── build_vector_db.py
│
├── retrieval/
│   ├── __init__.py
│   ├── retriever.py
│   ├── router.py
│   ├── hybrid_search.py
│   └── rbac.py
│
├── generation/
│   ├── __init__.py
│   ├── prompt.py
│   └── rag_chain.py
│
├── utils/
│   ├── confidence.py
│   └── citations.py
│
└── vectorstore/
    └── chroma_db/
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/enterprise-rag.git

cd enterprise-rag
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a .env file:

```env
MISTRAL_API_KEY=YOUR_MISTRAL_API_KEY
```

---

## Dataset

Place your files inside:

```text
data/

├── pdfs/
├── csvs/
└── logs/
```

Example:

```text
data/pdfs/finance_report.pdf
data/csvs/revenue.csv
data/logs/security_logs.json
```

---

## Build Vector Database

Run:

```bash
python -m ingestion.build_vector_db
```

This command:

* Loads PDFs
* Loads CSVs
* Loads JSON Logs
* Creates Embeddings
* Stores vectors inside ChromaDB

---

## Run Application

```bash
streamlit run app.py
```

Application will start at:

```text
http://localhost:8501
```

---

## User Roles

### Admin

Access:

* Finance
* Engineering
* HR
* Security

### Manager

Access:

* Engineering
* Reports

### Employee

Access:

* Reports

Example:

```json
{
  "john": "admin",
  "alice": "manager",
  "bob": "employee"
}
```

---

## Example Queries

### Finance

```text
What is the total revenue in Q2?
```

### Security

```text
Were there any security incidents reported?
```

### Compliance

```text
What compliance measures were reviewed?
```

### Forecasting

```text
What is the projected revenue for Q3?
```

---

## Example Output

```text
Answer:

No critical security incidents were reported during Q2.
All employee access requests were reviewed under RBAC policies.

Confidence: 0.95

Sources:

finance_report.pdf
```

---

## Security Features

### RBAC Enforcement

Documents are filtered before answer generation.

Only authorized users can access sensitive information.

### Sensitive Data Protection

Restricted departments cannot be queried by unauthorized users.

### Retrieval Filtering

Unauthorized documents are removed from retrieved context.

---

## Future Enhancements

* Hybrid Search (BM25 + Vector Search)
* Query Classification
* Metadata Filtering
* Multi-Hop Reasoning
* Re-Ranking
* Audit Logging
* FastAPI Backend
* Docker Deployment
* Kubernetes Deployment
* Multi-Tenant Support

---

## Author

Sairaj Balla

AI/ML Engineer | Computer Vision | NLP | Retrieval-Augmented Generation (RAG)

---

## License

MIT License
