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

app = FastAPI(
    title="ApiForge"
)

OUTPUT_DIR = "output"
os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)


@app.post("/generate")
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
def generate_scenarios_api(request: ScenarioRequest):

    scenarios = generate_scenarios(
        headers=request.headers,
        path_params=request.path_params,
        query_params=request.query_params,
        body_params=request.body_params,
    )

    result = []

    for idx, scenario in enumerate(
        scenarios,
        start=1
    ):

        curl = build_scenario_curl(
            request.method,
            request.url,
            scenario
        )

        result.append(
            {
                "scenario": idx,
                "curl": curl,
            }
        )

    return {
        "total": len(result),
        "scenarios": result,
    }