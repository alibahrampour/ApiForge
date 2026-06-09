from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from typing import List, Dict, Optional


class ScenarioRequest(BaseModel):
    method: str
    url: str

    headers: Optional[List[str]] = []
    path_params: Optional[List[str]] = []
    query_params: Optional[List[str]] = []
    body_params: Optional[List[str]] = []

    mode: str = "exhaustive"

class Route(BaseModel):
    url: str
    method: str


class GenerateRequest(BaseModel):
    routes: List[Route]
    headers: Dict[str, Any] = {}
    bodies: Optional[List[Dict[str, Any]]] = []
    queries: Optional[List[Dict[str, Any]]] = []