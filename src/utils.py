from itertools import combinations

def extract_route_name(url: str) -> str:
    parts = [p for p in url.split("/") if p]

    if not parts:
        return "request"

    return parts[-1].replace("-", "_")



def powerset(items):
    result = []

    for r in range(1, len(items) + 1):
        result.extend(combinations(items, r))

    return result


def generate_scenarios(
    headers,
    path_params,
    query_params,
    body_params
):
    scenarios = []

    header_sets = powerset(headers) if headers else [()]
    path_sets = powerset(path_params) if path_params else [()]
    query_sets = powerset(query_params) if query_params else [()]
    body_sets = powerset(body_params) if body_params else [()]

    for h in header_sets:
        for p in path_sets:
            for q in query_sets:
                for b in body_sets:

                    if not any([h, p, q, b]):
                        continue

                    scenarios.append(
                        {
                            "headers": list(h),
                            "path_params": list(p),
                            "query_params": list(q),
                            "body_params": list(b),
                        }
                    )

    return scenarios