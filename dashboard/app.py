import streamlit as st
import requests

st.title("SafeSight AI – Live Dashboard")

uploaded = st.file_uploader("Upload data for inference")

if uploaded:
    res = requests.post(
        "http://localhost:8000/predict",
        files={"file": uploaded.getvalue()}
    )
    st.json(res.json())
