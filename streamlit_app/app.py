# streamlit_app/app.py
import os

import requests
import streamlit as st

API_URL = os.environ.get("API_URL", "http://api:8000")
_DEFAULT_TIMEOUT = 30
try:
    REQUEST_TIMEOUT = int(os.environ.get("REQUEST_TIMEOUT_SECONDS", _DEFAULT_TIMEOUT))
except ValueError:
    REQUEST_TIMEOUT = _DEFAULT_TIMEOUT

st.title("SafeSight-AI | Real-Time Risk Detection")

file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png", "webp", "bmp"])
if file:
    try:
        res = requests.post(
            f"{API_URL}/predict",
            files={"file": (file.name, file, file.type)},
            timeout=REQUEST_TIMEOUT,
        )
        res.raise_for_status()
        data = res.json()
        risk_level = data.get("risk_level", "Unknown")
        st.metric("Risk Level", risk_level)
    except requests.exceptions.Timeout:
        st.error("Request timed out. The inference service may be unavailable.")
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the inference API. Check that the service is running.")
    except requests.exceptions.HTTPError as exc:
        st.error(f"API returned an error: {exc.response.status_code} – {exc.response.text}")
    except Exception as exc:
        st.error(f"Unexpected error: {exc}")
