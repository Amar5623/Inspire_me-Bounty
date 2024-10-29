# src/utils/metrics.py

from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(vector1, vector2):
    """
    Calculates cosine similarity between two vectors.
    """
    return cosine_similarity([vector1], [vector2])[0][0]

def evaluate_retrieval(results, ground_truth):
    """
    Evaluates retrieval performance using precision and recall.
    """
    relevant_results = [item for item in results if item in ground_truth]
    precision = len(relevant_results) / len(results) if results else 0
    recall = len(relevant_results) / len(ground_truth) if ground_truth else 0
    return {"precision": precision, "recall": recall}
