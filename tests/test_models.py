# tests/test_models.py
import unittest
from src.models.model_utils import get_text_embedding, get_image_embedding

class ModelTests(unittest.TestCase):

    def test_text_embedding(self):
        text = "Sample text for embedding"
        embedding = get_text_embedding(text)
        self.assertEqual(len(embedding), 384)  # Assuming a 384-dimensional embedding for SBERT

    # Placeholder for image embedding test
    def test_image_embedding(self):
        # You'd typically load a sample image here
        # image = Image.open("path/to/sample_image.jpg")
        # embedding = get_image_embedding(image)
        self.assertTrue(True)  # Image test placeholder

if __name__ == "__main__":
    unittest.main()
