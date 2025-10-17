import streamlit as st
import os
import random

st.title("📊 Dataset et Prétraitement")

st.markdown("""
### 📁 Source du dataset :
**Brain Tumor MRI Dataset (Kaggle)**  
- Classes : Glioma, Meningioma, Pituitary, No Tumor  
- Taille : ~8000 images

### 🧼 Prétraitement :
- Redimensionnement des images en (224, 224)
- Normalisation [0,1]
- Data Augmentation : rotation, zoom, flip, etc.
""")
st.image(os.getcwd() + "/src/images/output.png", caption="Exemple d’image IRM", use_container_width=True)

