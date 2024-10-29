# src/models/clip_model.py
from transformers import CLIPProcessor, CLIPModel
import torch

# Load CLIP model and processor
clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def generate_clip_embedding(image):
    """
    Generates an embedding for an image using the CLIP model.
    """
    inputs = clip_processor(images=image, return_tensors="pt")
    with torch.no_grad():
        embedding = clip_model.get_image_features(**inputs)
    return embedding.cpu().numpy().tolist()
