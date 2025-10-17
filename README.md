# BrainScan AI

## Contexte du projet
BrainScan AI est une startup marocaine innovante spécialisée dans les technologies d’imagerie médicale assistée par l’intelligence artificielle.  
L’objectif principal est de développer une application intelligente capable de :

- Analyser et classer les images IRM du cerveau pour détecter la présence de tumeurs cérébrales.
- Assister les médecins dans l’interprétation rapide et fiable des résultats.
- Optimiser le temps de diagnostic tout en réduisant les erreurs humaines.

Cette initiative s’inscrit dans une démarche visant à allier santé, innovation et IA pour renforcer la qualité et la rapidité des soins médicaux au Maroc.

---

## Structure du projet

```
BRAINCAN-DETECTION-DU-CANCER/
│
├── app/
│   ├── pages/
│   │   ├── 01_Présentation.py
│   │   ├── 02_Dataset_et_Pretaitement.py
│   │   ├── 03_Architecture_du_Modele.py
│   │   ├── 04_Résultats_et_Performances.py
│   │   ├── 05_Démo_Préduction.py
│   │   └── 06_A_Propos.py
│   │
│   └── app.py
│
├── data/
│   ├── processed/
│   └── raw/
│
├── models/
│   ├── best_model.keras
│   └── labelencoder.pkl
│
├── notebooks/
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_model_training.ipynb
│   ├── 03_evaluation.ipynb
│   └── 04_streamlit_demo.ipynb
│
├── src/
│
├── .gitignore
├── README.md
├── requirements.txt
└── temp.jpg

```

---

## Chargement et Prétraitement du Dataset

1. Importer les bibliothèques nécessaires (`numpy`, `opencv`, `os`, `sklearn`…).
2. Charger les images et vérifier leurs extensions (`jpeg`, `jpg`, `bmp`, `png`). Supprimer les fichiers invalides.
3. Utiliser un bloc `try-except` pour gérer les erreurs lors du chargement.
4. Explorer les classes (les noms des dossiers représentent les classes).
5. Mélanger les images et les labels dans deux listes correspondantes.
6. Redimensionner les images à une taille fixe (ex. 224×224) avec OpenCV.
7. Convertir les listes en tableaux NumPy exploitables par le CNN.
8. Visualiser le nombre d’images par classe et montrer des échantillons.
9. Vérifier l’équilibre entre les classes et rééquilibrer si nécessaire.
10. Encoder les labels (`LabelEncoder` ou `to_categorical`).
11. Diviser les données en ensembles d’entraînement et de test.
12. Normaliser les pixels dans la plage `[0,1]`.

---

## Conception du Modèle CNN

- Architecture typique :
  ```python
  Conv2D(32, (3,3), activation='relu', input_shape=(224,224,3))
  MaxPooling2D(2,2)
  Conv2D(64, (3,3), activation='relu')
  MaxPooling2D(2,2)
  Conv2D(128, (3,3), activation='relu')
  MaxPooling2D(2,2)
  Flatten()
  Dense(128, activation='relu')
  Dropout(0.5)
  Dense(4, activation='softmax')
  ```
- Choix des fonctions d’activation et de la couche de sortie.
- Compilation du modèle (`Adam`, `categorical_crossentropy`).
- Visualisation avec `model.summary()` et `plot_model()`.
- Définition des hyperparamètres : taux d’apprentissage, nombre d’époques, batch size.
- Mesure de la durée d’entraînement avec `time`.

---

## Entraînement et Évaluation

1. Entraînement avec `model.fit()`.
2. Sauvegarde du meilleur modèle via `ModelCheckpoint`.
3. Évaluation sur l’ensemble de test.
4. Visualisation des courbes d’apprentissage (accuracy / loss).
5. Matrice de confusion et rapport de classification.
6. Affichage d’exemples de prédictions correctes et incorrectes.

---

## Déploiement et Utilisation

- Fonction `predict_image(path)` pour tester une image.
- Sauvegarde du modèle entraîné (`.h5` ou `.pt`).
- Développement d’une interface Streamlit (`app.py`) pour tester les prédictions en temps réel.

---

## Documentation et Reproductibilité

- Ajout de commentaires explicatifs dans le code.
- Fichiers Markdown et notebooks pour expliquer chaque étape.
- Tâches planifiées dans Jira sous forme d’Epics et de tickets.

---

## Modalités pédagogiques

- Travail : Individuel  
- Durée : 5 jours  
- Période : Du 13/10/2025 au 17/10/2025 avant minuit

---

## Installation et Exécution

1. Cloner le projet :
   ```bash
   git clone https://github.com/OUSSAMAEDDERKAOUI/BrainScan-Detection-du-Cancer-Cerebral-par-CNN
   cd BrainScan-Detection-du-Cancer-Cerebral-par-CNN
   ```
2. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
3. Lancer l’interface Streamlit :
   ```bash
   streamlit run src/app.py
   ```

---

## License
Projet interne BrainScan AI – Tous droits réservés.


