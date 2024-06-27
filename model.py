import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the dataset
data = pd.read_csv("cancer_prediction_dataset.csv")

# Assuming the dataset has columns named 'Gender', 'Age', 'Smoking', 'Fatigue', 'Allergy', 'Target'
# and 'Target' is the column we want to predict
X = data[['Gender', 'Age', 'Smoking', 'Fatigue', 'Allergy']]
y = data['Target']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the trained model
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)
