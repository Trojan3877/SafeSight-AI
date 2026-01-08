# 🛡️ SafeSight AI — Production-Grade AI Safety System

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-API-green.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red.svg)](https://streamlit.io/)
[![CUDA](https://img.shields.io/badge/NVIDIA-CUDA-76B900.svg)](https://developer.nvidia.com/cuda-zone)
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue.svg)](https://www.docker.com/)
[![CI](https://img.shields.io/badge/GitHub-Actions-black.svg)](https://github.com/features/actions)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[![SafeSight-AI Repo](https://github-readme-stats.vercel.app/api/pin/?username=Trojan3877&repo=SafeSight-AI&theme=radical)](https://github.com/Trojan3877/SafeSight-AI)

 SafeSight-AI 🚨
**Production-Grade Computer Vision Risk Detection System**

SafeSight-AI is an end-to-end AI system designed to detect safety risks using computer vision.  
Built with **TensorFlow**, **Flask**, **Docker**, and **Streamlit**, it demonstrates enterprise-grade AI engineering practices.



 System Architecture
Streamlit UI → Flask API → TensorFlow Inference → Risk Engine



Core Features
- TensorFlow CV inference
- RESTful Flask API
- Human-in-the-loop Streamlit dashboard
- Dockerized microservices
- CI-validated testing pipeline


 Run Locally
```bash
docker compose -f docker/docker-compose.yml up --build

UI: http://localhost:8501
API: http://localhost:8000
Testing

Bash
pytest tests/
Engineering Highlights
Separation of concerns (UI / API / ML)
Risk scoring abstraction
CI-validated builds
Production-ready Docker setup
 Future Roadmap
Real-time video ingestion
Model versioning & A/B testing
Edge deployment (Jetson / iOS)
Observability metrics
👨‍💻 Author
Corey Leath
AI / ML Engineer | Computer Vision | MLOps