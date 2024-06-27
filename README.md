# Cancer_Prediction_Web_Application
# Files Description
app.py: The main Flask application that serves the web pages and handles predictions.
model_training.py: Script to train the Random Forest model and save it as a pickle file.
templates/index.html: HTML template for the web form.
cancer_prediction_dataset.csv: CSV file containing the dataset used for training the model.
model.pkl: The trained machine learning model saved as a pickle file.
# Requirements
pip install flask scikit-learn pandas
# The application will be available at http://127.0.0.1:5000/.
# Usage
1.Open your web browser and navigate to http://127.0.0.1:5000/.
2.Fill out the form with the following inputs:
Gender: Select Male or Female.
Age: Enter your age.
Smoking: Indicate if you smoke (0: No, 1: Yes).
Fatigue: Indicate if you experience fatigue (0: No, 1: Yes).
Allergy: Indicate if you have any allergies (0: No, 1: Yes).
3.Click on the "Predict" button.
4.The prediction result ("Cancer" or "No Cancer") will be displayed on the page.
