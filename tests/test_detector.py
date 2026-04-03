from src.detector import SafetyDetector


def test_detection_output():
    detector = SafetyDetector()
    events = detector.run_detection()
    assert isinstance(events, list)
    assert len(events) > 0


def test_detection_event_keys():
    """Each event must contain the required keys used downstream."""
    detector = SafetyDetector()
    for event in detector.run_detection():
        assert "zone" in event, "Event missing 'zone' key"
        assert "risk" in event, "Event missing 'risk' key"
        assert "type" in event, "Event missing 'type' key"


def test_detection_risk_in_range():
    """Risk scores must be a float in [0, 1]."""
    detector = SafetyDetector()
    for event in detector.run_detection():
        assert 0.0 <= event["risk"] <= 1.0, f"Risk score out of range: {event['risk']}"


def test_custom_threshold_env(monkeypatch):
    """DETECTION_THRESHOLD env var should be picked up by SafetyDetector."""
    monkeypatch.setenv("DETECTION_THRESHOLD", "0.5")
    detector = SafetyDetector()
    assert detector.threshold == 0.5

