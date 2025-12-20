from fastapi import FastAPI, UploadFile, File
from api.inference import predict

app = FastAPI(
    title="SafeSight AI API",
    description="Production-grade AI safety inference service",
    version="1.0.0"
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
async def run_prediction(file: UploadFile = File(...)):
    result = predict(await file.read())
    return result
