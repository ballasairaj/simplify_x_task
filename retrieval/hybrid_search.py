from rank_bm25 import BM25Okapi

def bm25_search(query, docs):

    corpus = [
        d.page_content.split()
        for d in docs
    ]

    bm25 = BM25Okapi(corpus)

    scores = bm25.get_scores(
        query.split()
    )

    ranked = sorted(
        zip(docs, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return [x[0] for x in ranked[:5]]