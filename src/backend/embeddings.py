# src/backend/embeddings.py
from sentence_transformers import SentenceTransformer

# Initialize embedding model (can be CLIP or Sentence-BERT based on project needs)
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')  # Efficient Sentence-BERT model

def generate_embedding(text: str):
    """
    Generates a vector embedding for a given text input.
    """
    return embedding_model.encode(text).tolist()
