from ddgs import DDGS


def search_web(
    query: str,
    max_results: int = 5,
)->list:
    results = DDGS().text(
        query,
        max_results=max_results,
    )

    if not results:
        return []

    items = []

    for result in results:
        items.append(
            {
                "title":result.get(
                    "title",
                    "",
                ),
                "url":result.get(
                    "href",
                    "",
                ),
                "snippet":result.get(
                    "body",
                    "",
                ),
            }
        )
    return items