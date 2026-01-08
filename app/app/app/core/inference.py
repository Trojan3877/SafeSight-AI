# app/core/inference.py
def run_inference(model, tensor):
    preds = model.predict(tensor)
    return preds