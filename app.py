import os
from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load the pre-trained model
# model = joblib.load("C:/Durham/2000 Applied Machine Learning/Lab4/Flask/fish_species_model.joblib")
current_dir = os.path.dirname(os.path.abspath(__file__))

# Update the model file path based on the current directory
model_file_path = os.path.join(current_dir, "fish_species_model.joblib")

# Load the model using the updated file path
model = joblib.load(model_file_path)

@app.route('/', methods=['GET', 'POST'])
def index():
    species = None
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
