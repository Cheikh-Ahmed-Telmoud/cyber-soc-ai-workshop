import streamlit as st
import pandas as pd
from scapy.all import sniff, IP
import joblib
import plotly.express as px
from datetime import datetime

st.set_page_config(page_title="CyberSOC AI", layout="wide", page_icon="🚨")
st.title("🚀 CyberSOC AI - Plateforme de Monitoring & Détection IA")

tabs = st.tabs(["Monitoring Live", "Analyse Dataset", "Détection IA", "Alerting", "Prévention"])

with tabs[0]:
    st.subheader("Capture Live")
    if st.button("Démarrer capture 10s"):
        packets = sniff(timeout=10)
        st.write(f"{len(packets)} paquets capturés")
        # Affichage simple des IPs sources
        srcs = [pkt[IP].src for pkt in packets if IP in pkt]
        st.bar_chart(pd.Series(srcs).value_counts())

with tabs[2]:
    st.subheader("Détection avec XGBoost")
    model = joblib.load("models/xgboost_cicids.pkl")
    uploaded = st.file_uploader("Upload CSV flow", type="csv")
    if uploaded:
        df = pd.read_csv(uploaded)
        pred = model.predict(df)
        st.success(f"Attaques détectées : {sum(pred != 'Benign')}")

