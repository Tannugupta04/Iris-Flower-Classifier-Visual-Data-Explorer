# 🌼 Iris Flower Classifier & Visual Data Explorer

This Streamlit web app allows users to **classify iris flower species** based on input features and provides a rich set of **interactive visualizations** to explore the famous [Iris dataset](https://archive.ics.uci.edu/ml/datasets/iris).

---

## 🔗 Link to the App

👉 [Click to Open the Iris Classifier Web App](https://celebal-datatscience-assignement-week-7-dhglfzlcaterwtuguvwhvm.streamlit.app/)


---

## 🚀 Features

### 🔍 Prediction
- Users can input Sepal and Petal measurements to predict the Iris species
- Displays predicted label and model confidence as a bar chart

### 📊 Visual Explorations

- **Tab 1 – Basic Stats**
  - Dataset preview
  - Species count plot

- **Tab 2 – Feature Analysis**
  - Histogram of selected feature
  - Violin plot by species
  - Box plot comparison

- **Tab 3 – Advanced Plots**
  - Correlation heatmap
  - Pair plot of all feature combinations
  - Feature means by species
  - Feature importance based on model

---

## 🧠 Machine Learning Model

- Model used: **Random Forest Classifier**
- Trained using `train_model.py` on the Iris dataset
- Model serialized using `joblib` as `iris_model.pkl`
- Input features:
  - Sepal Length
  - Sepal Width
  - Petal Length
  - Petal Width
- Output: Predicted Iris species (Setosa, Versicolor, Virginica)

---

## 🗂️ Project Structure

📁 iris-streamlit-app/
├── app.py # Streamlit app
├── train_model.py # Script to train and save model/data
├── iris_model.pkl # Trained RandomForest model
├── iris_data.csv # Preprocessed Iris dataset
├── pairplot.png # Pair plot image (generated at runtime)
├── requirements.txt # Required Python packages
└── README.md # Project overview (this file)
