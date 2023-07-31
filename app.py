import os
from flask import Flask, render_template, request
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# Load the pre-trained model using Pickle
model_file_path = "fish_species_model.pkl"

# Check if the model file exists, if not, train the model and save it using Pickle

try:
    with open(model_file_path, 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    data = pd.read_csv("Fish.csv")
    X = data.drop(columns=["Species"])
    y = data.Species

    # Create and train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    # Save the trained model to a file using Pickle
    with open(model_file_path, 'wb') as file:
        pickle.dump(model, file)

    # Load the model again to use the newly trained model
    with open(model_file_path, 'rb') as file:
        model = pickle.load(file)
port = int(os.environ.get('PORT', 5000))

@app.route('/', methods=['GET'])
def show_form():
    return render_template('index.html', species="None")

@app.route('/', methods=['POST'])
def predict_species():
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
    app.run(host='0.0.0.0', port=port, debug=True)
