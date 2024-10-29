# src/backend/database.py

import json
from pathlib import Path
from chromadb import Client

def get_db_connection():
    return Client()

def load_sample_data():
    db = get_db_connection()
    data_file = Path(__file__).parent / 'data' / 'sample_data.json'
    
    # Check if sample_data.json exists
    if not data_file.exists():
        print("Sample data file not found, skipping data load.")
        return
    
    with open(data_file, 'r') as f:
        data = json.load(f)
    
    # Get or create a collection
    collection = db.get_or_create_collection("sample_data")
    
    # Insert each item into the collection
    for item in data:
        collection.add(
            documents=[
                {
                    "id": item['id'],
                    "text": item['text'],
                    "image_path": item['image_path']
                }
            ]
        )
