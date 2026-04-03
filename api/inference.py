# api/inference.py
import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)


def run_inference(image_tensor: Any, model: Any) -> Any:
    """Run model inference on a pre-processed image tensor.

    Args:
        image_tensor: Tensor produced by the preprocessing step.
        model: A loaded ML model with a ``predict`` method.

    Returns:
        Raw model predictions.
    """
    predictions = model.predict(image_tensor)
    return predictions


def predict(image_bytes: bytes) -> Dict[str, Any]:
    """Entry-point for the FastAPI route: accepts raw image bytes and returns a
    risk prediction dictionary.

    This is a stub that should be replaced with a real model pipeline.
    It currently raises ``NotImplementedError`` so that callers receive a
    clear 500 error rather than a silent wrong result.

    Args:
        image_bytes: Raw bytes of the uploaded image file.

    Returns:
        A dict with at least a ``risk_level`` key.

    Raises:
        NotImplementedError: Until a real model is wired up.
    """
    raise NotImplementedError(
        "predict() is not yet implemented. Wire up a real model pipeline."
    )
