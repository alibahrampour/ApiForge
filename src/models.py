from pydantic import BaseModel
from typing import List, Dict, Any, Optional


class Route(BaseModel):
    url: str
    method: str


class GenerateRequest(BaseModel):
    routes: List[Route]

    headers: Dict[str, Any] = {}

    bodies: Optional[List[Dict[str, Any]]] = []

    queries: Optional[List[Dict[str, Any]]] = []


class ScenarioRequest(BaseModel):
    routes: List[Route]

    headers: Dict[str, Any] = {}

    bodies: Optional[List[Dict[str, Any]]] = []

    queries: Optional[List[Dict[str, Any]]] = []

    mode: str = "exhaustive"