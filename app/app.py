import streamlit as st

st.set_page_config(
    page_title="BrainScan - Documentation",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 BrainScan – Documentation du projet")
st.markdown("""
Bienvenue dans la documentation interactive du projet **BrainScan**.  
Ce projet vise à **détecter les tumeurs cérébrales à partir d’images IRM** grâce à un modèle de Deep Learning basé sur un CNN.

Utilise le **menu de gauche** pour naviguer entre les sections :
- Présentation du projet  
- Dataset et Prétraitement  
- Architecture du modèle  
- Résultats et performances  
- Démonstration de prédiction  
- À propos  
""")
