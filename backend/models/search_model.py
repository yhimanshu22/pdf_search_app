from pydantic import BaseModel
from typing import List

class SearchResult(BaseModel):
    chunk: str
    score: float

class SearchResponse(BaseModel):
    query: str
    results: List[SearchResult]
