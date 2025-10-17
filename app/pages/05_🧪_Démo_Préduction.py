import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
import os
import joblib
st.title("🧪 Démonstration de Prédiction")


model = load_model(os.getcwd() + "/models/best_model.keras")  
labelencoder = joblib.load(os.getcwd() + "/models/labelencoder.pkl")
class_names = labelencoder.classes_

def predict_image(path):
    img = cv2.imread(path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_resized = cv2.resize(img_rgb, (224, 224))
    img_resized = img_resized.astype('float32') / 255.0
    img_resized = np.expand_dims(img_resized, axis=0)
    
    pred_probs = model.predict(img_resized)
    pred_class_idx = np.argmax(pred_probs, axis=1)[0]
    pred_class_name = labelencoder.inverse_transform([pred_class_idx])[0]
    
    return img_rgb, pred_class_name, pred_probs[0]

st.title("BrainScan AI - Prédiction des tumeurs cérébrales")

uploaded_file = st.file_uploader("Choisir une image IRM", type=["jpg","jpeg","png","bmp"])

if uploaded_file is not None:
    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    img, pred_class, pred_probs = predict_image("temp.jpg")
    
    st.image(img, caption="Image test", use_column_width=True)
    st.success(f"Classe prédite : {pred_class}")
    
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(class_names, pred_probs, color='skyblue')
    ax.set_ylabel("Probabilité")
    ax.set_ylim(0,1)
    ax.set_title("Probabilités pour chaque classe")
    st.pyplot(fig)
