FROM nvidia/cuda:12.1.0-runtime-ubuntu22.04

WORKDIR /app
COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt

HEALTHCHECK --interval=30s --timeout=10s --start-period=15s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]

