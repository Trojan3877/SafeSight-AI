# 🛡️ SafeSight AI — Production-Grade AI Safety System

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-API-green.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red.svg)](https://streamlit.io/)
[![CUDA](https://img.shields.io/badge/NVIDIA-CUDA-76B900.svg)](https://developer.nvidia.com/cuda-zone)
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue.svg)](https://www.docker.com/)
[![CI](https://img.shields.io/badge/GitHub-Actions-black.svg)](https://github.com/features/actions)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🚀 Overview

**SafeSight AI** is a **production-ready AI safety and inference platform** designed to demonstrate **real-world ML engineering, system design, and deployment practices**.

This repository showcases:
- End-to-end AI inference
- REST APIs with FastAPI
- Live monitoring dashboards
- NVIDIA CUDA acceleration
- CI/CD automation
- Infrastructure-ready Docker builds
- Engineering documentation used in Big Tech environments

> 🎯 Built to **L6–L7 engineering standards**, not academic demos.

---

## 🧠 System Architecture
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/0b77a225-40af-4b06-8401-e3b33f9f9918" />

```mermaid
flowchart LR
    Client -->|REST| FastAPI
    FastAPI --> Inference
    Inference -->|CUDA| Model
    Model --> Metrics
    Metrics --> Dashboard
    CI --> Docker
    Docker --> Render


🏗️ Tech Stack
Layer	Technology
Language	Python 3.10+
API	FastAPI
ML	PyTorch
GPU	NVIDIA CUDA
Dashboard	Streamlit
Container	Docker
CI/CD	GitHub Actions
Automation	n8n
Deployment	Render / GPU-enabled infra

Repository Structure
SafeSight-AI/
│
├── api/
│   ├── main.py
│   ├── inference.py
│   └── schemas.py
│
├── dashboard/
│   └── app.py
│
├── model/
│   └── model.pt
│
├── n8n/
│   └── workflow.json
│
├── metrics.md
├── dailylog.md
├── CONTRIBUTING.md
├── Dockerfile
├── requirements.txt
└── README.md

Quick Start (Local)
git clone https://github.com/Trojan3877/SafeSight-AI
cd SafeSight-AI
pip install -r requirements.txt
uvicorn api.main:app --reload


Visit:

API → http://localhost:8000/docs

Dashboard → streamlit run dashboard/app.py
📊 Metrics & Performance

See 👉 metrics.md

Avg Inference: ~42ms

P95 Latency: <70ms

Accuracy: 93%+

GPU-accelerated inference supported

🔁 CI/CD Pipeline

Automatic build on push

Code validation

Docker compatibility checks

Production-ready workflow

🤖 Automation (n8n)

Health checks

Inference monitoring

Alert pipelines

See 👉 n8n/workflow.json

☁️ Deployment (Render / GPU)
docker build -t safesight-ai .
docker run --gpus all -p 8000:8000 safesight-ai


Supports:

Render

GPU-enabled cloud

On-prem NVIDIA systems

🧭 Engineering Philosophy

This project was built to demonstrate:

Production thinking

System design clarity

ML + backend integration

Reliability and observability

Recruiter-visible engineering maturity

📬 Contact

Corey Leath
Senior Undergraduate — Software Development
Aspiring AI / ML Engineer

GitHub: https://github.com/Trojan3877

LinkedIn: (recommended to add here)

⭐ If you're a recruiter: this repo reflects how I build in real environments, not toy projects.


