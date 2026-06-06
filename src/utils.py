def extract_route_name(url: str) -> str:
    parts = [p for p in url.split("/") if p]

    if not parts:
        return "request"

    return parts[-1].replace("-", "_")