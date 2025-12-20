![Status](https://img.shields.io/badge/status-production--ready-success)
![Level](https://img.shields.io/badge/engineering--level-L7-blueviolet)
![Python](https://img.shields.io/badge/python-3.10+-blue)
![Framework](https://img.shields.io/badge/framework-PyTorch-red)
![API](https://img.shields.io/badge/api-FastAPI-green)
![Container](https://img.shields.io/badge/container-Docker-blue)
![MLOps](https://img.shields.io/badge/mlops-MLflow-orange)
![Automation](https://img.shields.io/badge/automation-n8n-purple)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

# 🛡️ SafeSight-AI  
**AI-Powered Safety Intelligence Platform**
🚀 Overview

SafeSight-AI is a production-oriented AI safety intelligence system that detects, explains, and escalates safety-critical events using:

Computer Vision

Machine Learning

Large Language Models (LLMs)

Event-driven automation

This repository is designed to reflect real-world AI systems used in Big Tech, smart infrastructure, and safety-critical domains, not academic demos.

🧠 Why This Is L7-Level

✔ End-to-end system ownership
✔ ML + LLM integration (not just inference)
✔ Explainable AI (human-readable reasoning)
✔ Automation-first design
✔ Metrics, logging, and governance built-in

This project demonstrates senior system design thinking, not just model training.
System Architecture
flowchart TD
    A[Camera / Image / Sensor Input] --> B[Vision Model<br/>(PyTorch + OpenCV)]
    B --> C[Risk Classification<br/>Confidence Scoring]
    C --> D[LLM Reasoning Layer<br/>(GPT-4o via LangChain)]
    D --> E[Structured Event JSON]
    E --> F[n8n Automation Engine]
    F --> G[Alerts<br/>Slack / Email / Webhook]
    F --> H[Audit Logs]
    F --> I[Human Review Dashboard]
Design philosophy:
Detect → Explain → Automate → Keep humans in control

🧩 Core Components
🔍 Computer Vision & ML

CNN / detection-based inference

Confidence thresholding

Low-latency prediction

Bias-aware preprocessing

🧠 LLM Explainability

Converts ML outputs into plain-English explanations

Generates safety summaries

Structured prompts to avoid hallucinations

Supports audits & compliance

⚙️ Automation (n8n)

Risk-based escalation workflows

Alert routing (Slack, Email, Webhooks)

Daily safety summaries

Human-in-the-loop approvals

📊 Observability & Governance

MLflow experiment tracking

Metrics reporting

Engineering logs

Ethical AI safeguards

📈 Metrics Snapshot

See METRICS.md for full details.

Metric	Result
Accuracy	~94%
F1 Score	~92%
False Positives	< 5%
Avg Inference Latency	~120ms
Automation Success Rate	~98%
