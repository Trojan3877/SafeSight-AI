# app/core/risk_engine.py
from typing import List


def compute_risk(predictions: List[List[float]]) -> str:
    """Return a risk level string based on the highest prediction confidence.

    Args:
        predictions: A 2-D list where ``predictions[0]`` contains per-class
            confidence scores produced by the model.

    Returns:
        "HIGH", "MEDIUM", or "LOW".

    Raises:
        ValueError: If *predictions* is empty or contains no scores.
    """
    if not predictions or not predictions[0]:
        raise ValueError("predictions must be a non-empty 2-D list.")

    confidence = max(predictions[0])

    if confidence > 0.85:
        return "HIGH"
    elif confidence > 0.60:
        return "MEDIUM"
    return "LOW"