# src/models/model_utils.py
from .clip_model import generate_clip_embedding
from .sbert_model import generate_sbert_embedding

def get_text_embedding(text: str):
    """
    Returns an embedding for the input text using Sentence-BERT.
    """
    return generate_sbert_embedding(text)

def get_image_embedding(image):
    """
    Returns an embedding for the input image using CLIP.
    """
    return generate_clip_embedding(image)
