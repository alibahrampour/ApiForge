from fastapi import FastAPI
import json
import os

from models import Route
from models import GenerateRequest

from utils import extract_route_name

from curl_builder import build_curl
from postman_builder import build_postman_item

from models import ScenarioRequest
from utils import generate_scenarios
from curl_builder import build_scenario_curl

from datetime import datetime


app = FastAPI(
    title="ApiForge"
)

OUTPUT_DIR = "output"
os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)


@app.post("/generate curl")
def generate(data: GenerateRequest):

    routes = data.routes
    headers = data.headers
    bodies = data.bodies or []
    queries = data.queries or []

    if not bodies:
        bodies = [None]

    if not queries:
        queries = [None]

    curl_output = []
    postman_items = []

    total = 0

    for r_idx, route in enumerate(routes, start=1):

        route_name = extract_route_name(
            route.url
        )

        for b_idx, body in enumerate(
                bodies,
                start=1
        ):

            for q_idx, query in enumerate(
                    queries,
                    start=1
            ):

                total += 1

                request_name = (
                    f"{route.method.upper()}_"
                    f"{route_name}_"
                    f"R{r_idx}_"
                    f"B{b_idx if body else 0}_"
                    f"Q{q_idx if query else 0}"
                )

                curl = build_curl(
                    url=route.url,
                    method=route.method,
                    headers=headers,
                    body=body,
                    query=query
                )

                curl_output.append(
                    f"# {request_name}\n{curl}\n"
                )

                postman_items.append(
                    build_postman_item(
                        route,
                        headers,
                        body,
                        query,
                        request_name
                    )
                )

    curl_file = os.path.join(
        OUTPUT_DIR,
        "curls.sh"
    )

    with open(
        curl_file,
        "w",
        encoding="utf-8"
    ) as f:
        f.write(
            "\n\n".join(
                curl_output
            )
        )

    postman_collection = {
        "info": {
            "name": "Generated Collection",
            "schema":
                "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
        },
        "item": postman_items
    }

    postman_file = os.path.join(
        OUTPUT_DIR,
        "postman_collection.json"
    )

    with open(
        postman_file,
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            postman_collection,
            f,
            ensure_ascii=False,
            indent=2
        )

    return {
        "generated_requests": total,
        "curl_file": curl_file,
        "postman_file": postman_file
    }


@app.post("/generate-scenarios")
def generate_scenarios_api(
    request: ScenarioRequest
):

    scenarios = generate_scenarios(
        routes=request.routes,
        headers=request.headers,
        bodies=request.bodies,
        queries=request.queries,
        mode=request.mode
    )

    result = []
    postman_items = []

    for idx, scenario in enumerate(
        scenarios,
        start=1
    ):

        curl = build_scenario_curl(
            route=scenario["route"],
            headers=scenario["headers"],
            body=scenario["body"],
            query=scenario["query"]
        )

        request_name = f"Scenario_{idx}"

        result.append(
            {
                "scenario": idx,
                "method": scenario["route"].method,
                "url": scenario["route"].url,
                "headers": scenario["headers"],
                "body": scenario["body"],
                "query": scenario["query"],
                "curl": curl
            }
        )

        postman_items.append(
            build_postman_item(
                scenario["route"],
                scenario["headers"],
                scenario["body"],
                scenario["query"],
                request_name
            )
        )

    postman_collection = {
        "info": {
            "name": "Scenario Collection",
            "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
        },
        "item": postman_items
    }

    postman_file = os.path.join(
        OUTPUT_DIR,
        "scenario_collection.json"
    )

    with open(
        postman_file,
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            postman_collection,
            f,
            ensure_ascii=False,
            indent=2
        )

    generated_at = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    html_rows = ""

    for item in result:

        query_text = json.dumps(
            item["query"],
            ensure_ascii=False,
            indent=2
        ) if item["query"] else "-"

        body_text = json.dumps(
            item["body"],
            ensure_ascii=False,
            indent=2
        ) if item["body"] else "-"

        html_rows += f"""
        <tr>
            <td>{item['scenario']}</td>
            <td>{item['method']}</td>
            <td>{item['url']}</td>
            <td><pre>{query_text}</pre></td>
            <td><pre>{body_text}</pre></td>
            <td><pre>{item['curl']}</pre></td>
        </tr>
        """

    html_content = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>ApiForge Scenario Report</title>

<style>

body {{
    font-family: Arial, sans-serif;
    background: #f5f5f5;
    padding: 30px;
}}

h1 {{
    margin-bottom: 20px;
}}

.card {{
    background: white;
    padding: 20px;
    border-radius: 8px;
    margin-bottom: 20px;
}}

table {{
    width: 100%;
    border-collapse: collapse;
    background: white;
}}

th {{
    background: #2d3748;
    color: white;
}}

th, td {{
    border: 1px solid #ddd;
    padding: 10px;
    vertical-align: top;
}}

pre {{
    margin: 0;
    white-space: pre-wrap;
    word-break: break-word;
}}

</style>

</head>

<body>

<h1>ApiForge Scenario Report</h1>

<div class="card">
    <h2>Summary</h2>

    <p><strong>Mode:</strong> {request.mode}</p>

    <p><strong>Total Scenarios:</strong> {len(result)}</p>

    <p><strong>Generated At:</strong> {generated_at}</p>
</div>

<div class="card">
    <h2>Artifacts</h2>

    <p>
        <strong>Postman Collection:</strong>
        {postman_file}
    </p>
</div>

<table>

<tr>
    <th>#</th>
    <th>Method</th>
    <th>URL</th>
    <th>Query</th>
    <th>Body</th>
    <th>Curl</th>
</tr>

{html_rows}

</table>

</body>
</html>
"""

    html_file = os.path.join(
        OUTPUT_DIR,
        "scenario_report.html"
    )

    with open(
        html_file,
        "w",
        encoding="utf-8"
    ) as f:
        f.write(html_content)

    return {
        "mode": request.mode,
        "total": len(result),
        "html_file": html_file,
        "postman_file": postman_file
    }