import streamlit as st
import os
st.title("📈 Résultats et Performances")

st.subheader("📊 Rapport de classification")

st.markdown("""
| Classe | Précision | Recall | F1-score |
|:-------|:----------:|:-------:|:---------:|
| Glioma | 0.94 | 0.73 | 0.82 |
| Meningioma | 0.68 | 0.90 | 0.77 |
| Pituitary | 0.97 | 0.98 | 0.97 |
| No Tumor | 0.95 | 0.84 | 0.89 |

**Accuracy globale :** 0.86  
**F1-score moyen pondéré :** 0.86
""")
st.subheader("🧠 Interprétation des résultats")

st.markdown("""
- Le modèle atteint une **accuracy globale de 86%**, ce qui est satisfaisant pour une première version.  
- Les classes **Pituitary** et **No Tumor** sont bien reconnues (F1-score > 0.9).  
- Les classes **Glioma** et **Meningioma** montrent un léger déséquilibre entre précision et rappel.  
- Une amélioration possible : utiliser des techniques de rééquilibrage des classes ou un ajustement de seuil.
""")

st.image(os.getcwd() + "/src/images/courbes_apprentissage.png", caption="Courbes de précision et de perte pendant l'entraînement", use_container_width=True)


st.subheader("🧾 Prédictions correctes et incorrectes")

st.markdown("""
Cette figure illustre des exemples d’images où le modèle a correctement ou incorrectement classé les tumeurs.
""")

pred_img_path = os.getcwd() +"/src/images/prédictions_correctes_incorrectes.png"

if os.path.exists(pred_img_path):
    st.image(pred_img_path, caption="Exemples de prédictions correctes et erronées", use_container_width=True)
else:
    st.warning("⚠️ L’image `prédictions_correctes_incorrectes.png` est introuvable. Ajoute-la dans `src/images/` pour l’afficher ici.")


