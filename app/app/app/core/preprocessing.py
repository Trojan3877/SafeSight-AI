# app/core/preprocessing.py
from typing import Any


def preprocess(image: Any) -> Any:
    """Pre-process an uploaded image into a model-ready tensor.

    This is a stub implementation.  Replace with real preprocessing logic
    (e.g. resizing, normalization, tensor conversion) when a model is available.

    Args:
        image: A Flask ``FileStorage`` object or raw image data.

    Returns:
        The pre-processed tensor (currently returns the raw image unchanged).
    """
    return image
