# app/core/risk_engine.py
def compute_risk(predictions):
    confidence = max(predictions[0])
    if confidence > 0.85:
        return "HIGH"
    elif confidence > 0.60:
        return "MEDIUM"
    return "LOW"