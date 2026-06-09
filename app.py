import streamlit as st

from retrieval.retriever import retrieve

from retrieval.rbac import filter_docs

from generation.rag_chain import generate_answer

from utils.citations import build_citations

from utils.confidence import confidence_score

st.title(
    "Enterprise RAG Assistant"
)

username = st.selectbox(
    "User",
    [
        "john",
        "alice",
        "bob"
    ]
)

query = st.text_input(
    "Ask Question"
)

if st.button("Submit"):

    docs = retrieve(query)

    docs = filter_docs(
        username,
        docs
    )

    context = "\n".join(
        [d.page_content for d in docs]
    )

    answer = generate_answer(
        query,
        context
    )

    citations = build_citations(
        docs
    )

    confidence = confidence_score(
        docs
    )

    st.write("### Answer")

    st.write(answer)

    st.write(
        f"Confidence: {confidence}"
    )

    st.write(
        "### Sources"
    )

    for source in citations:

        st.write(source)