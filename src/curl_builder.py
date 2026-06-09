import json
from urllib.parse import urlencode


def build_curl(
    url: str,
    method: str,
    headers: dict,
    body: dict | None,
    query: dict | None
):

    final_url = url

    if query:
        final_url += "?" + urlencode(query)

    curl = (
        f"curl --location "
        f"--request {method.upper()} "
        f"'{final_url}'"
    )

    for k, v in headers.items():
        curl += (
            f" \\\n--header '{k}: {v}'"
        )

    if body:
        curl += (
            f" \\\n--data "
            f"'{json.dumps(body, ensure_ascii=False)}'"
        )

    return curl

def build_scenario_curl(
    route,
    headers,
    body,
    query
):

    return build_curl(
        url=route.url,
        method=route.method,
        headers=headers,
        body=body,
        query=query
    )