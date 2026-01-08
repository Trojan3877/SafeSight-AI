# app/core/inference.py
def run_inference(image_tensor, model):
    predictions = model.predict(image_tensor)
    return predictions