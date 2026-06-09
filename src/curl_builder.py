import json
from urllib.parse import urlencode


def build_curl(
    url: str,
    method: str,
    headers: dict | None = None,
    body: dict | None = None,
    query: dict | None = None
):
    final_url = url

    if query:
        final_url += "?" + urlencode(query)

    curl = (
        f"curl --location "
        f"--request {method.upper()} "
        f"'{final_url}'"
    )

    if headers:
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
    method: str,
    url: str,
    scenario: dict
):
    """
    scenario example:

    {
        "headers": ["Authorization"],
        "query_params": ["page", "size"],
        "body_params": ["name"]
    }
    """

    headers = {
        header: f"{header}_value"
        for header in scenario.get("headers", [])
    }

    query = {
        param: f"{param}_value"
        for param in scenario.get("query_params", [])
    }

    body = {
        param: f"{param}_value"
        for param in scenario.get("body_params", [])
    }

    return build_curl(
        url=url,
        method=method,
        headers=headers if headers else None,
        body=body if body else None,
        query=query if query else None,
    )