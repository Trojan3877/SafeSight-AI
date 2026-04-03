import os

import requests
import streamlit as st

API_URL = os.environ.get("API_URL", "http://localhost:8000")
_DEFAULT_TIMEOUT = 30
try:
    REQUEST_TIMEOUT = int(os.environ.get("REQUEST_TIMEOUT_SECONDS", _DEFAULT_TIMEOUT))
except ValueError:
    REQUEST_TIMEOUT = _DEFAULT_TIMEOUT

st.title("SafeSight AI – Live Dashboard")

uploaded = st.file_uploader("Upload data for inference")

if uploaded:
    try:
        res = requests.post(
            f"{API_URL}/predict",
            files={"file": (uploaded.name, uploaded.getvalue(), uploaded.type)},
            timeout=REQUEST_TIMEOUT,
        )
        res.raise_for_status()
        st.json(res.json())
    except requests.exceptions.Timeout:
        st.error("Request timed out. The inference service may be unavailable.")
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the inference API. Check that the service is running.")
    except requests.exceptions.HTTPError as exc:
        st.error(f"API returned an error: {exc.response.status_code} – {exc.response.text}")
    except Exception as exc:
        st.error(f"Unexpected error: {exc}")

