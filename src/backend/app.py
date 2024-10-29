# src/backend/app.py

from fastapi import FastAPI
from .database import load_sample_data
from .search import search_similar_content

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    load_sample_data()

@app.get("/search")  # Make sure this matches the test URL
async def search(query: str):
    results = await search_similar_content(query)
    return {"results": results}
