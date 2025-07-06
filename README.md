## 🔗 Link to the App

You can access the deployed Streamlit application here:

👉 [Click to Open the Iris Classifier App](https://celebal-datatscience-assignement-week-7-dhglfzlcaterwtuguvwhvm.streamlit.app/)

> 🌐 Hosted via [Streamlit Community Cloud](https://streamlit.io/cloud)



# 🌼 Iris Flower Classifier & Visual Data Explorer

This Streamlit web app allows users to **classify iris flower species** based on input features and provides a rich set of **interactive visualizations** to explore the famous [Iris dataset](https://archive.ics.uci.edu/ml/datasets/iris).

---

## 🚀 Features

🔍 **Prediction**  
- Users can input Sepal and Petal measurements to predict the Iris species  
- Displays predicted label and model confidence as a bar chart

📊 **Visual Explorations**  
- **Tab 1 – Basic Stats**:  
  View sample data and class distribution

- **Tab 2 – Feature Analysis**:  
  - Histogram  
  - Violin Plot  
  - Box Plot  
  (with smart captions to interpret distributions)

- **Tab 3 – Advanced Plots**:  
  - Correlation heatmap  
  - Pair plot of all features  
  - Feature means by species  
  - Feature importance from trained model

---

## 🧠 ML Model Details

- Model used: **Random Forest Classifier**
- Trained using `train_model.py` on the Iris dataset
- Serialized with `joblib` and loaded in `app.py`

---

## 🗂️ File Structure

