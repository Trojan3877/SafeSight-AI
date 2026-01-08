# app/api/routes.py
from flask import Blueprint, request, jsonify
from app.models.loader import load_model
from app.core.preprocessing import preprocess
from app.core.inference import run_inference
from app.core.risk_engine import compute_risk

api = Blueprint("api", __name__)
model = load_model()

@api.route("/predict", methods=["POST"])
def predict():
    image = request.files["image"]
    tensor = preprocess(image)
    preds = run_inference(model, tensor)
    risk = compute_risk(preds)
    return jsonify({"risk_level": risk})