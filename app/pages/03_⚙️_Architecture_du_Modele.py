import streamlit as st
import os

st.title("⚙️ Architecture du Modèle")

st.markdown("""
Le modèle BrainScan repose sur un **Convolutional Neural Network (CNN)** conçu pour extraire les caractéristiques visuelles des IRM.
""")

# Sous-titre
st.subheader("🧠 Architecture du modèle CNN")

# Code du modèle
st.code("""
Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3))
MaxPooling2D(2,2)
Conv2D(64, (3,3), activation='relu')
MaxPooling2D(2,2)
Conv2D(128, (3,3), activation='relu')
MaxPooling2D(2,2)
Flatten()
Dense(128, activation='relu')
Dropout(0.5)
Dense(4, activation='softmax')
""", language='python')

# Hyperparamètres
st.markdown("""
### ⚙️ Hyperparamètres :
- Batch size : 32  
- Epochs : 30
- Optimizer : Adam  
- Loss : Categorical Crossentropy  
""")

# Image
st.image(os.path.join(os.getcwd(), "src/images/cnn.png"),
         caption="Architecture du modèle CNN",
         use_container_width=True)
