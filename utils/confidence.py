def confidence_score(
    retrieved_docs
):

    if len(retrieved_docs) >= 5:
        return 0.95

    if len(retrieved_docs) >= 3:
        return 0.80

    return 0.60