![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![PyTorch](https://img.shields.io/badge/pytorch-deep%20learning-red)
![CUDA](https://img.shields.io/badge/nvidia-cuda-green)
![LLM](https://img.shields.io/badge/llm-llama--3-purple)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![CI](https://img.shields.io/badge/ci-github%20actions-success)
![Deploy](https://img.shields.io/badge/deploy-render-orange)
![MLOps](https://img.shields.io/badge/mlops-production-black)
![Level](https://img.shields.io/badge/engineering%20level-L7-gold)


**SafeSight-AI** is a production-grade, AI-driven safety monitoring system designed to **detect hazardous events in real time**, generate **human-readable risk explanations using Llama-3**, and trigger **automated alerts** via workflow orchestration.

Built with **PyTorch**, **CUDA**, **LLMs**, **CI/CD**, and **automation-first design**, this project demonstrates **Staff-level AI Engineering and MLOps practices**.

---

## 🧠 Core Features

* 🔥 **Deep Learning Safety Event Detection**
* 🤖 **Llama-3 LLM Risk Explanation (NVIDIA CUDA)**
* ⚡ **Low-latency inference**
* 🔁 **n8n Automation (Slack / Email / API)**
* 📊 **Metrics + Monitoring**
* 🧪 **Unit Tests + CI/CD**
* ☁️ **Deployable on Render**
* 🐳 **Docker (CPU & CUDA)**

---

## 🏗️ AI-Generated System Design

```
┌──────────────────┐
│   Sensors / Feeds│
└─────────┬────────┘
          ↓
┌──────────────────┐
│ ML Safety Detector│   ← PyTorch
└─────────┬────────┘
          ↓
┌──────────────────┐
│ Llama-3 LLM Engine│   ← NVIDIA CUDA
│ Risk Explanation  │
└─────────┬────────┘
          ↓
┌──────────────────┐
│ Alert Engine      │
│ (Severity Logic)  │
└─────────┬────────┘
          ↓
┌──────────────────┐
│ n8n Workflow      │
│ Slack / Email /API│
└──────────────────┘
```

---

## ⚡ Quick Start (CPU)

```bash
git clone https://github.com/Trojan3877/SafeSight-AI
cd SafeSight-AI
pip install -r requirements.txt
python src/main.py
```

---

## 🚀 CUDA / NVIDIA (Llama-3 Enabled)

### Build & Run (GPU)

```bash
docker build -f docker/Dockerfile.cuda -t safesight-gpu .
docker run --gpus all safesight-gpu
```

✔ Uses **CUDA 12+**
✔ Auto device mapping
✔ Optimized FP16 inference

---

## ☁️ Render Deployment

```bash
render deploy
```

> **Note:** Render hosts the API + orchestration layer
> GPU inference supported via cloud GPU providers (RunPod / Lambda / AWS)

---

## 🧪 Tests & CI/CD

```bash
pytest tests/
```

✔ GitHub Actions
✔ Auto-tested on every push
✔ Production-safe merges

---

## 📊 Metrics Snapshot

| Metric          | Value     |
| --------------- | --------- |
| Precision       | **92.4%** |
| Recall          | **89.7%** |
| F1 Score        | **91.0%** |
| GPU Latency     | **~38ms** |
| False Positives | **3.1%**  |

---

## 🔔 Automation (n8n)

* Slack alerts
* Email notifications
* API hooks
* Extensible workflows

---

## 🧠 Tech Stack

* **Python 3.10**
* **PyTorch**
* **CUDA / NVIDIA**
* **Meta Llama-3**
* **FastAPI**
* **Docker**
* **GitHub Actions**
* **n8n**
* **Render**

---

## 👤 Author

**Corey Leath**
Senior Undergraduate — Software Development (Web & Mobile)
AI / ML Engineer | MLOps | LLM Systems
GitHub: [https://github.com/Trojan3877](https://github.com/Trojan3877)


