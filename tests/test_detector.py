from src.detector import SafetyDetector

def test_detection_output():
    detector = SafetyDetector()
    events = detector.run_detection()
    assert isinstance(events, list)
    assert len(events) > 0
