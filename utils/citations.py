def build_citations(docs):

    sources = []

    for d in docs:

        sources.append(
            d.metadata.get(
                "source",
                "unknown"
            )
        )

    return list(set(sources))