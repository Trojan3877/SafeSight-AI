import os
from typing import Any, Dict, List


class SafetyDetector:
    def __init__(self) -> None:
        self.threshold: float = float(
            os.environ.get("DETECTION_THRESHOLD", 0.75)
        )

    def run_detection(self) -> List[Dict[str, Any]]:
        # Simulated detection events
        return [
            {"zone": "Warehouse A", "risk": 0.82, "type": "Slip Hazard"},
            {"zone": "Site B", "risk": 0.91, "type": "No PPE"},
        ]

