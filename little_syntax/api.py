from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel

from little_syntax.runner import run_source


app = FastAPI(
    title="Little Syntax API",
    description="API for running Little Syntax code.",
    version="0.1.0",
)


class RunRequest(BaseModel):
    source: str


class RunResponse(BaseModel):
    output: list[str]
    errors: list[str]
    variables: dict[str, Any]


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/run", response_model=RunResponse)
def run_code(request: RunRequest):
    result = run_source(request.source)

    return {
        "output": result["output"],
        "errors": result["errors"],
        "variables": result["variables"],
    }
