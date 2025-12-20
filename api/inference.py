import torch

model = torch.load("model/model.pt", map_location="cpu")
model.eval()

def predict(image_bytes):
    # Placeholder preprocessing
    with torch.no_grad():
        output = model(image_bytes)
    return {
        "prediction": output.argmax().item(),
        "confidence": float(output.max())
    }
