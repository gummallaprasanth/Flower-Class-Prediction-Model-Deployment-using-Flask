# Flower Class Prediction Using Flask 


### Overview
This project provides a web application for predicting the species of flowers from the Iris dataset using machine learning. The application takes user input for flower measurements and returns the predicted species.

### Features

User-friendly web interface

Input fields for flower measurements (sepal length, sepal width, petal length, petal width)

Real-time prediction using a trained machine learning model

Model trained on the Iris dataset


## Technologies Used

Backend: Flask

Machine Learning: Scikit-learn

Frontend: HTML

Data Visualization: Matplotlib (optional for graphs)

## Requirements

Python 3.x

Flask

scikit-learn

pandas

numpy

Other dependencies (listed in requirements.txt)



## Usage

Navigate to the home page of the application.

Input the flower measurements:

Sepal Length

Sepal Width

Petal Length

Petal Width

Click the "Predict" button to get the predicted species.

The predicted species will be displayed on the same page.

## Model Training

The machine learning model is pre-trained using the Iris dataset. If you wish to retrain the model, ensure you have the dataset available. Here’s a brief outline of the training process:

Load the Iris dataset using pandas.

Preprocess the data (if necessary).

Split the data into training and testing sets.

Train a model using Scikit-learn (e.g., Decision Tree, Random Forest).

Save the trained model using joblib or pickle.

## Deployment

To deploy the app, you may consider using platforms like Heroku or AWS. Ensure you have the necessary environment variables and configurations set up.
