class RiskExplainer:
    def explain(self, event):
        return (
            f"High-risk event detected: {event['type']} "
            f"in {event['zone']} with risk score {event['risk']}."
        )
