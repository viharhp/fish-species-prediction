# Fish Prediction Web Application

The Fish Prediction web application is built using Flask, a Python web framework, to predict the species of a fish based on its measurements. The application uses a pre-trained machine learning model to make predictions.

## How to Use

1. Clone the repository or download the source code.

2. Install the required Python packages using `pip`:

` pip install Flask scikit-learn pandas `

3. Prepare your fish data in a CSV file. The CSV file should have columns: "Weight," "Length1," "Length2," "Length3," "Height," "Width," and "Species."

4. Train the machine learning model using your fish data. Edit the `train_model.py` script with the path to your CSV file and the appropriate model training code. Then, run the script to train the model and save it to a file named `fish_species_model.joblib`:

` python train_model.py `

5. Ensure you have the trained model file (`fish_species_model.joblib`) in the project directory.

6. Run the Flask application:

` python app.py `

7. Open your web browser and go to `http://localhost:5000/` to access the Fish Prediction web application.

8. Enter the fish measurements (Weight, Length1, Length2, Length3, Height, and Width) into the input fields on the web page.

9. Click the "Predict" button to make a prediction.

10. The predicted fish species will be displayed below the form.

## Customization

- If you want to use a different trained model, replace the `fish_species_model.joblib` file with your own trained model file. Ensure that the model's input features match the order of the input fields in the HTML form.

- Customize the `train_model.py` script to use your own data and model training pipeline for better predictions.

## Acknowledgments

This project uses the Flask web framework and scikit-learn library. Thanks to the respective communities for developing and maintaining these powerful tools.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to modify, enhance, or distribute this project according to the terms of the MIT License.


