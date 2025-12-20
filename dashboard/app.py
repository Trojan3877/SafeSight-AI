import streamlit as st
import requests

st.title("SafeSight AI – Live Inference")

uploaded = st.file_uploader("Upload Image")

if uploaded:
    response = requests.post(
        "http://localhost:8000/predict",
        files={"file": uploaded.getvalue()}
    )
    st.json(response.json())
