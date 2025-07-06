
import streamlit as st
import joblib
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="🌸 Iris Classifier & Data Explorer", layout="wide")

# Load model and data
model = joblib.load('iris_model.pkl')
iris_df = pd.read_csv('iris_data.csv')
features = iris_df.columns[:-1]
species = iris_df['species'].unique()

# --- TITLE ---
st.title("🌼 Iris Flower Classifier & Visual Data Explorer")

# --- SIDEBAR ---
st.sidebar.header(" Input Flower Measurements")
sepal_length = st.sidebar.slider("Sepal Length (cm)", 4.0, 8.0, 5.4)
sepal_width = st.sidebar.slider("Sepal Width (cm)", 2.0, 4.5, 3.4)
petal_length = st.sidebar.slider("Petal Length (cm)", 1.0, 7.0, 1.3)
petal_width = st.sidebar.slider("Petal Width (cm)", 0.1, 2.5, 0.2)

input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

# --- PREDICTION ---
st.subheader("🔍 Prediction")
if st.button("Predict"):
    # prediction = model.predict(input_data)[0]
    prediction_idx = model.predict(input_data)[0]
    species_name = iris_df['species'].unique()[prediction_idx]

    probs = model.predict_proba(input_data)[0]
    # st.success(f"✅ Predicted Species: **{prediction.capitalize()}**")
    st.success(f"✅ Predicted Species: **{species_name.capitalize()}**")

    prob_df = pd.DataFrame(probs.reshape(1, -1), columns=model.classes_)
    st.bar_chart(prob_df.T)
    st.caption("🔹 The taller the bar, the higher the model's confidence in that species.")

# --- DATA VISUALIZATION TABS ---
st.header("📊 Visual Explorations of the Iris Dataset")

tab1, tab2, tab3 = st.tabs(["🔢 Basic Stats", "🧪 Feature Analysis", "📌 Advanced Plots"])

# -------------------------------
# TAB 1: Basic Stats
# -------------------------------
with tab1:
    st.subheader("Dataset Overview")
    st.dataframe(iris_df.head(10))
    st.markdown("This dataset contains **150 Iris flower records** with 4 features and 3 species.")
    
    st.subheader("📈 Species Count")
    fig, ax = plt.subplots()
    sns.countplot(data=iris_df, x='species', palette='Set2', ax=ax)
    st.pyplot(fig)
    st.caption("🔹 Shows how balanced the dataset is across species.")

# -------------------------------
# TAB 2: Feature Analysis
# -------------------------------
with tab2:
    selected_feature = st.selectbox("Select a feature to analyze:", features)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📦 Histogram")
        fig, ax = plt.subplots()
        sns.histplot(iris_df[selected_feature], kde=True, color='skyblue', ax=ax)
        st.pyplot(fig)
        st.caption(f"🔹 Distribution of **{selected_feature}**. Peaks show common values.")

    with col2:
        st.subheader("🎻 Violin Plot by Species")
        fig, ax = plt.subplots()
        sns.violinplot(data=iris_df, x='species', y=selected_feature, palette="Pastel1", ax=ax)
        st.pyplot(fig)
        st.caption(f"🔹 Violin shows how **{selected_feature}** varies per species and its density.")

    st.subheader("📊 Box Plot")
    fig, ax = plt.subplots()
    sns.boxplot(data=iris_df, x='species', y=selected_feature, palette='coolwarm', ax=ax)
    st.pyplot(fig)
    st.caption(f"🔹 Box shows median and spread of **{selected_feature}** values per species.")

# -------------------------------
# TAB 3: Advanced Plots
# -------------------------------
with tab3:
    st.subheader("🔗 Correlation Heatmap")
    fig, ax = plt.subplots()
    corr = iris_df[features].corr()
    sns.heatmap(corr, annot=True, cmap="YlGnBu", ax=ax)
    st.pyplot(fig)
    st.caption("🔹 Shows how strongly features are related. 1 = strongly correlated.")

    st.subheader("📌 Pair Plot")
    with st.spinner("Generating pair plot..."):
        pair_plot = sns.pairplot(iris_df, hue="species", palette="husl")
        pair_plot.savefig("pairplot.png")
        st.image("pairplot.png", use_column_width=True)
        st.caption("🔹 Each subplot shows a scatter plot between two features, colored by species.")

    st.subheader("🌟 Feature Means by Species")
    feature_means = iris_df.groupby('species').mean()
    st.bar_chart(feature_means)
    st.caption("🔹 How each feature averages per species. Helps differentiate them.")

    st.subheader("🧠 Feature Importance (from Model)")
    importances = model.feature_importances_
    importance_df = pd.DataFrame({'Feature': features, 'Importance': importances})
    importance_df = importance_df.sort_values(by='Importance', ascending=False)

    fig, ax = plt.subplots()
    sns.barplot(x='Importance', y='Feature', data=importance_df, palette='viridis', ax=ax)
    st.pyplot(fig)
    st.caption("🔹 Features the model found most useful for prediction.")

# Footer
st.markdown("---")
st.markdown("🚀 Created with [Streamlit](https://streamlit.io/) | Dataset: UCI Iris")
