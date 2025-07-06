# import pandas as pd
# from sklearn.datasets import load_iris
# from sklearn.ensemble import RandomForestClassifier
# import joblib

# # Load data and train model
# iris = load_iris()
# X, y = iris.data, iris.target
# model = RandomForestClassifier()
# model.fit(X, y)

# # Save the model
# joblib.dump(model, 'iris_model.pkl')

# train_model.py
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import joblib

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, 'iris_model.pkl')

# Save dataset as DataFrame for app use
df = pd.DataFrame(X, columns=iris.feature_names)
df['species'] = pd.Series(y).map({i: name for i, name in enumerate(iris.target_names)})
df.to_csv('iris_data.csv', index=False)

print("✅ Model and dataset saved.")
