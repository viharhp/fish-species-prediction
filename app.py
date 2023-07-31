import os
from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

app = Flask(__name__)

# Load the dataset
data_file_path = os.path.join(os.path.dirname(__file__), "Fish.csv")
data = pd.read_csv(data_file_path)
X = data.drop(columns=["Species"])
y = data.Species

# Create and train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save the trained model to a file
with open('fish_species_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

@app.route('/', methods=['GET', 'POST'])
def index():
    species = "None"
    if request.method == 'POST':
        weight = float(request.form['weight'])
        length1 = float(request.form['length1'])
        length2 = float(request.form['length2'])
        length3 = float(request.form['length3'])
        height = float(request.form['height'])
        width = float(request.form['width'])

        # Use the loaded model to make the prediction
        data = [[weight, length1, length2, length3, height, width]]
        species = model.predict(data)[0]

    return render_template('index.html', species=species)

if __name__ == '__main__':
    app.run(debug=True)
