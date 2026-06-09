from itertools import combinations, product


def extract_route_name(url: str) -> str:
    parts = [p for p in url.split("/") if p]

    if not parts:
        return "request"

    return parts[-1].replace("-", "_")


def generate_scenarios(
    routes,
    headers,
    bodies,
    queries,
    mode="exhaustive"
):

    if not bodies:
        bodies = [None]

    if not queries:
        queries = [None]

    scenarios = []

    if mode == "minimal":

        for route in routes:

            scenarios.append(
                {
                    "route": route,
                    "headers": headers,
                    "body": bodies[0],
                    "query": queries[0]
                }
            )

        return scenarios

    if mode == "pairwise":

        max_size = max(
            len(routes),
            len(bodies),
            len(queries)
        )

        for i in range(max_size):

            scenarios.append(
                {
                    "route": routes[i % len(routes)],
                    "headers": headers,
                    "body": bodies[i % len(bodies)],
                    "query": queries[i % len(queries)]
                }
            )

        return scenarios

    # exhaustive

    for route, body, query in product(
        routes,
        bodies,
        queries
    ):
        scenarios.append(
            {
                "route": route,
                "headers": headers,
                "body": body,
                "query": query
            }
        )

    return scenarios