from src.detector import SafetyDetector
from src.alert_engine import AlertEngine

try:
    from src.src.llm_llama3 import Llama3RiskExplainer as RiskExplainerCls
except ImportError:
    from src.llm_guard import RiskExplainer as RiskExplainerCls  # type: ignore[assignment]


def main():
    detector = SafetyDetector()
    alerts = AlertEngine()
    llm = RiskExplainerCls()

    events = detector.run_detection()

    for event in events:
        explanation = llm.explain(event)
        alerts.dispatch(event, explanation)

if __name__ == "__main__":
    main()
