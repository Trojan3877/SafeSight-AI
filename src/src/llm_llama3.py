from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class Llama3RiskExplainer:
    def __init__(self):
        self.model_name = "meta-llama/Meta-Llama-3-8B-Instruct"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            torch_dtype=torch.float16,
            device_map="auto"
        )

    def explain(self, event):
        prompt = f"""
        Explain this safety risk clearly:
        Event: {event}
        """
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
        output = self.model.generate(**inputs, max_new_tokens=100)
        return self.tokenizer.decode(output[0], skip_special_tokens=True)
