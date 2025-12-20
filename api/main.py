from fastapi import FastAPI, UploadFile, File
from api.inference import predict

app = FastAPI(
    title="SafeSight AI",
    description="Production AI Safety Inference API",
    version="1.0.0"
)

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict")
async def predict_route(file: UploadFile = File(...)):
    result = predict(await file.read())
    return result

