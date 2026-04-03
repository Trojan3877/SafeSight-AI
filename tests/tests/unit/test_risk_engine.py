# tests/unit/test_risk_engine.py
import pytest

from app.app.app.core.risk_engine import compute_risk


def test_high_risk():
    preds = [[0.9, 0.1]]
    assert compute_risk(preds) == "HIGH"


def test_medium_risk():
    preds = [[0.7, 0.3]]
    assert compute_risk(preds) == "MEDIUM"


def test_low_risk():
    preds = [[0.4, 0.6]]
    assert compute_risk(preds) == "LOW"


def test_empty_predictions_raises():
    with pytest.raises(ValueError):
        compute_risk([])


def test_empty_inner_list_raises():
    with pytest.raises(ValueError):
        compute_risk([[]])
