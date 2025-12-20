import torch

model = torch.load("model/model.pt", map_location="cpu")
model.eval()

def predict(data):
    with torch.no_grad():
        output = model(data)
    return {
        "prediction": int(output.argmax()),
        "confidence": float(output.max())
    }
