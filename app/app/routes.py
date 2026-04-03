# app/api/routes.py
import logging

from flask import Blueprint, request, jsonify
from app.models.loader import load_model
from app.core.preprocessing import preprocess
from app.core.inference import run_inference
from app.core.risk_engine import compute_risk

logger = logging.getLogger(__name__)

api = Blueprint("api", __name__)
model = load_model()


@api.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image file provided."}), 400

    image = request.files["image"]

    if image.filename == "":
        return jsonify({"error": "Empty filename."}), 400

    try:
        tensor = preprocess(image)
        preds = run_inference(model, tensor)
        risk = compute_risk(preds)
    except ValueError as exc:
        logger.warning("Invalid input: %s", exc)
        return jsonify({"error": str(exc)}), 422
    except Exception as exc:
        logger.exception("Prediction failed: %s", exc)
        return jsonify({"error": "Internal server error."}), 500

    return jsonify({"risk_level": risk})