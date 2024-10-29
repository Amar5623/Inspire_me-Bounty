# tests/test_utils.py
import unittest
from src.utils.metrics import calculate_similarity, evaluate_retrieval

class UtilsTests(unittest.TestCase):

    def test_calculate_similarity(self):
        vec1 = [1, 2, 3]
        vec2 = [1, 2, 3]
        similarity = calculate_similarity(vec1, vec2)
        self.assertAlmostEqual(similarity, 1.0, places=2)

    def test_evaluate_retrieval(self):
        results = ["doc1", "doc2", "doc3"]
        ground_truth = ["doc1", "doc3", "doc5"]
        metrics = evaluate_retrieval(results, ground_truth)
        self.assertEqual(metrics["precision"], 2 / 3)
        self.assertEqual(metrics["recall"], 2 / 3)

if __name__ == "__main__":
    unittest.main()
