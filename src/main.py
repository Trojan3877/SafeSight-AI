from detector import SafetyDetector
from alert_engine import AlertEngine
from llm_llama3 import Llama3RiskExplainer

def main():
    detector = SafetyDetector()
    alerts = AlertEngine()
    llm = Llama3RiskExplainer()

    events = detector.run_detection()

    for event in events:
        explanation = llm.explain(event)
        alerts.dispatch(event, explanation)

if __name__ == "__main__":
    main()
