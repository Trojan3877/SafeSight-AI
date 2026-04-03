import logging
from typing import Any, Dict

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

logger = logging.getLogger(__name__)


class Llama3RiskExplainer:
    def __init__(self) -> None:
        self.model_name = "meta-llama/Meta-Llama-3-8B-Instruct"
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_name,
                torch_dtype=torch.float16,
                device_map="auto",
            )
        except Exception as exc:
            logger.error(
                "Failed to load Llama-3 model '%s': %s. "
                "Falling back to rule-based explanations.",
                self.model_name,
                exc,
            )
            self.tokenizer = None
            self.model = None

    def explain(self, event: Dict[str, Any]) -> str:
        """Generate a natural-language explanation for the given safety event.

        Falls back to a rule-based description if the LLM is unavailable.

        Args:
            event: Dictionary describing the detected hazard.

        Returns:
            A human-readable explanation string.
        """
        if self.model is None or self.tokenizer is None:
            return (
                f"High-risk event detected: {event.get('type', 'Unknown')} "
                f"in {event.get('zone', 'Unknown')} "
                f"with risk score {event.get('risk', 'N/A')}."
            )

        prompt = (
            "Explain this safety risk clearly:\n"
            f"Event: {event}\n"
        )
        try:
            inputs = self.tokenizer(prompt, return_tensors="pt").to(
                self.model.device
            )
            output = self.model.generate(**inputs, max_new_tokens=100)
            return self.tokenizer.decode(output[0], skip_special_tokens=True)
        except Exception as exc:
            logger.exception("LLM inference failed: %s", exc)
            return (
                f"High-risk event detected: {event.get('type', 'Unknown')} "
                f"in {event.get('zone', 'Unknown')} "
                f"with risk score {event.get('risk', 'N/A')}."
            )

