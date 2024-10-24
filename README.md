# Heart Failure Prediction Using Random Forest

![screenshot](imgs/heart.jpg)

## Overview
This project involves the analysis and prediction of heart failure risk using a Random Forest machine learning model. The model is trained on customized data, including various patient health metrics, to predict the likelihood of heart failure. The goal is to provide a tool that can assist healthcare professionals in identifying high-risk patients.

## Table of Contents
Overview
Features
Project Structure
Installation
Usage
Dataset
Model Details
Evaluation
Results
Contributing
License
Features


## Data Preprocessing: 
Handles missing values, normalization, and feature engineering.
Model Training: Utilizes the Random Forest algorithm for classification.
Feature Importance: Identifies the most significant predictors of heart failure.
Prediction: Provides heart failure risk predictions for new patients.
Evaluation: Includes model evaluation metrics such as accuracy, precision, recall, and ROC-AUC.

## Project Structure
~~~python
Heart_Failure_Prediction_V2 (Important files)
| Backend                                                 |
| - app.py                                                |
| - utils/machine_learning.py                             |
| - utils/predictBP.py                                    |
| - utils/prediction.py                                   |
| Frontend                                                |
| - templates/additional_info.html                        |
| - templates/info.html                                   |
| - templates/personal_info.html                          |
| - templates/result.html                                 |
| - static/styles.css                                     |
| Machine Learning                                        |
| - Machine_Learning/Generate_Dataset.ipynb               |
| - Machine_Learning/Heart_Failure_Analysis.ipynb         |
| - Machine_Learning/Machine_Learning_Random_Forest.ipynb |
| Utilities                                               |
| - utils/ageCalculate.py                                 |
| - utils/bmi.py                                          |
| Documentation                                           |
| - README.md                                             |
| - requirements.txt                                      |
| Trained Model                                           |
| - utils/random_forest_model_v2.pkl                            |
~~~

## Installation
Clone the repository:
~~~python
git clone https://github.com/MakMohanK/Heart_Failure_Prediction_V2.git
~~~

## Navigate to the project directory:
~~~python
cd Heart_Failure_Prediction_V2
~~~
## Create a virtual environment:

~~~python
python -m venv venv
~~~
## Activate the virtual environment:

### On Windows:

~~~python
venv\Scripts\activate
~~~

### On macOS/Linux:
~~~python
source venv/bin/activate

~~~

## Install the dependencies:
~~~python
pip install -r requirements.txt
~~~

# Usage
## Run the Flask application:
~~~python
python3 app.py
~~~

Access the application:

Open your web browser and navigate to http://127.0.0.1:5000/.

## Upload Data & Predict:

Upload patient data and get predictions on the likelihood of heart failure.

## Dataset
The dataset used in this project is a customized collection of patient health metrics, including features like age, blood pressure, cholesterol levels, and more. It is stored in data/heart_failure_custom_data.csv.

## Model Details
The model is a Random Forest classifier trained to predict heart failure. The training process includes:

## Hyperparameter Tuning: 
Optimized for best performance.
Cross-Validation: Ensures model robustness.
Feature Importance: Highlights key predictors of heart failure.
Evaluation
The model is evaluated using various metrics:

## Accuracy: 
Measures the overall correctness of predictions.
Precision & Recall: Evaluates the balance between false positives and false negatives.
ROC-AUC Curve: Assesses the model’s discrimination ability.
Results
The Random Forest model achieved an accuracy of 100% on the custom test data, with a precision of 100% and recall of 100%. The ROC-AUC score was W.