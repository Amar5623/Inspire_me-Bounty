# src/backend/search.py
from .database import get_db_connection

async def search_similar_content(query):
    db = get_db_connection()
    collection = db.get_or_create_collection("inspirations")

    results = collection.query(
        query_texts=[query],
        n_results=5  # Number of results to fetch
    )
    return results