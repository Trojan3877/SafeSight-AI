# streamlit_app/app.py
st.title("SafeSight AI – Real-Time Safety Monitor")

uploaded = st.file_uploader("Upload frame")
if uploaded:
    response = requests.post(API_URL, files={"image": uploaded})
    st.metric("Risk Score", response.json()["risk_score"])