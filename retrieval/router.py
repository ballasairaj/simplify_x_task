def route_query(query):

    q = query.lower()

    if "salary" in q:
        return "hr"

    if "security" in q:
        return "security"

    if "revenue" in q:
        return "finance"

    return "reports"