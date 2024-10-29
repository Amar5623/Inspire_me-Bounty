# tests/test_backend.py
import unittest
from fastapi.testclient import TestClient
from src.backend.app import app

class BackendTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    def test_search_endpoint(self):
        response = self.client.get("/search?query=sunrise")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        print("Response JSON:", data)
        self.assertIn("results", data)  # Adjust based on response structure
