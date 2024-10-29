# src/utils/data_loader.py
import os
from .config import DATA_PATH
from ..models.sbert_model import generate_sbert_embedding

def load_text_data():
    """
    Loads text data from the specified folder and generates embeddings.
    """
    text_data = []
    for filename in os.listdir(DATA_PATH["text"]):
        with open(os.path.join(DATA_PATH["text"], filename), 'r') as file:
            content = file.read()
            embedding = generate_sbert_embedding(content)
            text_data.append({"filename": filename, "content": content, "embedding": embedding})
    return text_data
