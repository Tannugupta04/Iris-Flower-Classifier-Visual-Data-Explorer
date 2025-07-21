Developed a web application using Streamlit to deploy a trained machine learning model. The app should allow users to input data, receive predictions, and understand model outputs through visualizations. This helped me to learn how to make your models accessible and interactive.



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

└── asi # Virtual environment 


## How to Use the App

### Step 1: Input Flower Measurements

Use the sidebar sliders on the left side of the app to enter your flower's measurements:

- Sepal Length (cm): Choose between 4.0 – 8.0  
- Sepal Width (cm): Choose between 2.0 – 4.5  
- Petal Length (cm): Choose between 1.0 – 7.0  
- Petal Width (cm): Choose between 0.1 – 2.5  

These values represent the characteristics of an Iris flower you want to classify.

---

### Step 2: Make a Prediction

After setting the values:

1. Click the **"Predict"** button  
2. The app will use a trained Random Forest model to predict the Iris species  
3. You'll see:
   - The predicted Iris species (e.g., Setosa, Versicolor, or Virginica)
   - A bar chart displaying the model's confidence for each class

---

### Step 3: Explore Visualizations

Below the prediction section, the app offers interactive data visualizations organized into three tabs:

| Tab Name        | Description |
|-----------------|-------------|
| Basic Stats     | View sample data and distribution of species in the dataset |
| Feature Analysis| Select a feature to see histogram, violin plot, and box plot comparisons across species |
| Advanced Plots  | View correlation heatmap, pair plots, feature means by species, and feature importance from the model |

Each chart includes a short description to help interpret the data.

---

Tip: Try adjusting input values and observe how predictions and visualizations change, especially for petal length and width — they strongly influence the model.


## How the Visualizations Work

The app includes several interactive charts and plots that help users understand the Iris dataset and the behavior of the classification model. These visualizations are organized into three tabs.

---

### Tab 1: Basic Stats

#### Dataset Preview  
Displays the first 10 rows of the dataset to give users an idea of the structure, feature names, and values.

#### Species Count  
A bar chart showing the number of samples for each Iris species.  
**Purpose**: To check if the dataset is balanced or skewed toward a specific class.

---

### Tab 2: Feature Analysis

This tab allows users to explore how a selected feature (e.g., *Petal Length*) varies across different species using three different plot types:

#### Histogram  
Displays the distribution of a selected feature for all samples.  
**Purpose**: To identify common values and understand the spread of the feature.

#### Violin Plot by Species  
Shows the distribution and density of the selected feature for each species.  
**Purpose**: Helps compare how each species differs in the selected feature.

#### Box Plot  
Displays the median, quartiles, and outliers for the selected feature across species.  
**Purpose**: Quickly assess central tendency and variation per species.

---

### Tab 3: Advanced Plots

#### Correlation Heatmap  
Displays the correlation coefficients between features (e.g., Sepal Width vs Petal Width).  
**Purpose**: To identify which features are strongly related and potentially redundant.

#### Pair Plot  
Creates a grid of scatter plots for every pair of features, color-coded by species.  
**Purpose**: Helps visualize relationships and separability between features across species.

#### Feature Means by Species  
Bar chart showing the average value of each feature grouped by species.  
**Purpose**: Highlights how feature values differ across species, useful for classification.

#### Feature Importance (from Model)  
Bar plot displaying how important each feature is according to the trained Random Forest model.  
**Purpose**: Helps users understand which features have the most influence on the prediction.

---

These visualizations make it easy to not only predict a species but also build intuition about the data, model behavior, and underlying patterns within the Iris dataset.

