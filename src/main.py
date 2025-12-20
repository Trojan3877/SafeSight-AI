from detector import SafetyDetector
from alert_engine import AlertEngine
from llm_guard import RiskExplainer

def main():
    detector = SafetyDetector()
    alert_engine = AlertEngine()
    llm = RiskExplainer()

    events = detector.run_detection()

    for event in events:
        explanation = llm.explain(event)
        alert_engine.dispatch(event, explanation)

if __name__ == "__main__":
    main()
