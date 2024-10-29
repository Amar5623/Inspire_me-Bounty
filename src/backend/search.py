# src/backend/search.py
from .database import get_db_connection

def search_similar_content(query_embedding):
    """
    Searches ChromaDB for content similar to the provided query embedding.
    """
    db = get_db_connection()
    
    # Perform similarity search in ChromaDB
    results = db.query_vector(
        vector=query_embedding,
        n=10  # Returns the top 10 similar results
    )
    
    # Transform results into a format suitable for the response
    formatted_results = [{"id": item['id'], "score": item['score'], "content": item['content']} for item in results]
    return formatted_results
