# streamlit_app/app.py
import streamlit as st
import requests

st.title("SafeSight-AI | Real-Time Risk Detection")

file = st.file_uploader("Upload Image")
if file:
    res = requests.post("http://api:8000/predict", files={"image": file})
    st.metric("Risk Level", res.json()["risk_level"])