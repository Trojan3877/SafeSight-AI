# tests/unit/test_risk_engine.py
from app.core.risk_engine import compute_risk

def test_high_risk():
    preds = [[0.9, 0.1]]
    assert compute_risk(preds) == "HIGH"