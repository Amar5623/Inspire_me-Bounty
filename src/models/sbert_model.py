# src/models/sbert_model.py
from sentence_transformers import SentenceTransformer

sbert_model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_sbert_embedding(text):
    """
    Generates an embedding for text using Sentence-BERT.
    """
    return sbert_model.encode(text).tolist()
