# 🛡️ SafeSight – Project Overview

## 🎯 Purpose
SafeSight is an AI-powered Computer Vision prototype designed to assist visually impaired users in navigating environments safely by detecting and identifying objects in real time. It simulates real-world accessibility solutions using a modular Python stack and lays the foundation for future mobile or cloud deployment.

## 📐 System Design Goals
- Real-time object detection via a webcam or test images
- Lightweight Flask server to simulate device interface
- Modular codebase for easy expansion (mobile, audio alerts, cloud backend)
- Ethical AI usage to enhance accessibility and safety

## 🔧 Technology Stack (Summarized)
- **Python** – Core language for backend and logic
- **TensorFlow/Keras** – Object detection model (e.g., MobileNet, SSD, or YOLO)
- **OpenCV** – Image processing and camera input handling
- **Flask** – Local web server to simulate device output or dashboard

## 🧱 Architecture Summary
- `app/`: Core logic including model handling and web routes
- `camera_stream.py`: Streams or simulates image input
- `model_utils.py`: Loads TensorFlow model and performs inference
- `templates/`: Contains Flask-rendered HTML for UI
- `static/`: Stylesheets and potential JS (future enhancements)
- `saved_model/`: Folder to hold pre-trained models
- `test_images/`: Local test samples for inference

## 🔮 Future Enhancements
- Firebase-based cloud storage and analytics
- Audio alerts or TTS (text-to-speech) support
- Streamlit front-end or Flutter mobile interface
- Model optimization for mobile and edge devices

## 🧑‍💼 Created By
**Corey Leath**  
Dual Bachelor's Student – Artificial Intelligence & Computer Science  
[LinkedIn Profile](https://linkedin.com/in/corey-leath)
