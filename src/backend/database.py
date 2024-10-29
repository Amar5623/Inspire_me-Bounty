import json
from pathlib import Path
from chromadb import Client
import os

def get_db_connection():
    return Client()

def load_sample_data():
    data_file = os.path.join(os.path.dirname(__file__), 'data', 'sample_data.json')
    with open(data_file, 'r') as f:
        data = json.load(f)
    
    db = get_db_connection()
    collection = db.get_or_create_collection("inspirations")

    for item in data:
        collection.add(
            ids=[item["id"]],
            documents=[item["content"]],
            metadatas=[{"source": item["source"], "image_path": item["image_path"]}]
        )
