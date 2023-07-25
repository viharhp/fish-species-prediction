import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv("https://raw.githubusercontent.com/viharhp/fish-species-prediction/main/Fish.csv")
data.info()
data.head()

X = data.drop(columns = ["Species"])
y = data.Species

# Create and train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save the trained model to a file
joblib.dump(model, 'fish_species_model.joblib')