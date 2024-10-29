# app.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from typing import List, Dict
import json
import os

app = FastAPI()

# Mount the images folder as static
app.mount("/images", StaticFiles(directory="src/backend/data/images"), name="images")

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load sample data from sample_data.json
sample_data_path = os.path.join("src", "backend", "data", "sample_data.json")

with open(sample_data_path, "r") as file:
    sample_data: List[Dict] = json.load(file)

@app.get("/search")
async def search(query: str):
    # Mock search functionality: Filter items in sample_data based on the query
    search_results = [
        {
            "id": data["id"],
            "text": data["text"],
            "image_path": f"images/{data['image_path'].split('/')[-1]}",
            "source": data["source"]
        }
        for data in sample_data if query.lower() in data["text"].lower()
    ]
    
    return {"results": search_results}
