import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)


class AlertEngine:
    def dispatch(self, event: Dict[str, Any], explanation: str) -> None:
        """Log a safety alert with its LLM-generated explanation.

        Args:
            event: Dictionary containing at least ``zone``, ``type``, and
                ``risk`` keys describing the detected hazard.
            explanation: Human-readable explanation produced by the risk
                explainer.
        """
        logger.warning(
            "SAFETY ALERT | zone=%s type=%s risk=%.2f | %s",
            event.get("zone", "unknown"),
            event.get("type", "unknown"),
            event.get("risk", 0.0),
            explanation,
        )

