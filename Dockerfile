FROM pytorch/pytorch:1.12.1-cuda11.3-cudnn8-runtime
RUN apt-get update && apt-get install -y libsm6 libxrender1 libxext6
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "demo.py", "--test", "examples/test_image.jpg"]
