import os
from typing import Any, Dict, List


class SafetyDetector:
    def __init__(self) -> None:
        _default_threshold = 0.75
        try:
            self.threshold: float = float(
                os.environ.get("DETECTION_THRESHOLD", _default_threshold)
            )
        except ValueError:
            self.threshold = _default_threshold

    def run_detection(self) -> List[Dict[str, Any]]:
        # Simulated detection events
        return [
            {"zone": "Warehouse A", "risk": 0.82, "type": "Slip Hazard"},
            {"zone": "Site B", "risk": 0.91, "type": "No PPE"},
        ]

