class SafetyDetector:
    def __init__(self):
        self.threshold = 0.75

    def run_detection(self):
        # Simulated detection events
        return [
            {"zone": "Warehouse A", "risk": 0.82, "type": "Slip Hazard"},
            {"zone": "Site B", "risk": 0.91, "type": "No PPE"}
        ]
