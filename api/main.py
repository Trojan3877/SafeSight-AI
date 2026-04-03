import os
import logging

from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse
from api.inference import predict

logger = logging.getLogger(__name__)

# Maximum accepted upload size: 10 MB
MAX_FILE_SIZE = int(os.environ.get("MAX_FILE_SIZE_BYTES", 10 * 1024 * 1024))
ALLOWED_CONTENT_TYPES = {"image/jpeg", "image/png", "image/webp", "image/bmp"}

app = FastAPI(
    title="SafeSight AI",
    description="Production AI Safety Inference API",
    version="1.0.0"
)


@app.get("/health")
def health() -> dict:
    return {"status": "healthy"}


@app.post("/predict")
async def predict_route(file: UploadFile = File(...)) -> JSONResponse:
    # Validate content type
    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(
            status_code=415,
            detail=f"Unsupported file type '{file.content_type}'. "
                   f"Allowed types: {sorted(ALLOWED_CONTENT_TYPES)}",
        )

    contents = await file.read()

    # Validate file size
    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail=f"File size {len(contents)} bytes exceeds the "
                   f"{MAX_FILE_SIZE}-byte limit.",
        )

    if len(contents) == 0:
        raise HTTPException(status_code=400, detail="Uploaded file is empty.")

    try:
        result = predict(contents)
    except Exception as exc:
        logger.exception("Inference failed: %s", exc)
        raise HTTPException(status_code=500, detail="Inference failed.") from exc

    return JSONResponse(content=result)

