import streamlit as st
import joblib
from feature_extraction import extract_features

model = joblib.load("phishing_model.pkl")

st.title("Phishing URL Detector")

url = st.text_input("Enter URL")

if st.button("Check URL"):

    features = extract_features(url)

    prediction = model.predict([features])[0]

    if prediction == 1:
        st.error("⚠️ Phishing URL")
    else:
        st.success("✅ Legitimate URL")