# tests/test_backend.py
import unittest
from fastapi.testclient import TestClient
from src.backend.app import app

client = TestClient(app)

class BackendTests(unittest.TestCase):

    def test_search_endpoint(self):
        response = self.client.get("/search?query=sunrise")  # Ensure this matches the endpoint
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
