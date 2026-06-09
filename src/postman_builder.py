import json


def build_postman_item(
    route,
    headers,
    body,
    query,
    request_name
):


    url_object = {
        "raw": route.url,
        "host": [route.url]
    }

    if query:
        url_object["query"] = [
            {
                "key": k,
                "value": str(v)
            }
            for k, v in query.items()
        ]

    request = {
        "name": request_name,
        "request": {
            "method": route.method.upper(),
            "header": [
                {
                    "key": k,
                    "value": str(v)
                }
                for k, v in headers.items()
            ],
            "url": url_object
        }
    }

    if body:
        request["request"]["body"] = {
            "mode": "raw",
            "raw": json.dumps(
                body,
                ensure_ascii=False,
                indent=2
            )
        }

    return request