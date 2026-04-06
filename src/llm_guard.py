from typing import Any, Dict


class RiskExplainer:
    def explain(self, event: Dict[str, Any]) -> str:
        """Return a concise human-readable description of a safety event.

        Args:
            event: Dictionary with keys ``type``, ``zone``, and ``risk``.

        Returns:
            A formatted explanation string.

        Raises:
            ValueError: If required keys are missing from *event*.
        """
        required_keys = {"type", "zone", "risk"}
        missing = required_keys - event.keys()
        if missing:
            raise ValueError(f"Event is missing required keys: {missing}")

        return (
            f"High-risk event detected: {event['type']} "
            f"in {event['zone']} with risk score {event['risk']}."
        )

