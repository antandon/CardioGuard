import numpy as np
import pickle

# Step 1: Load the trained Random Forest model
model_filename = "./utils/random_forest_model_v2.pkl"  # Replace with your model file name
with open(model_filename, 'rb') as file:
    rf_model = pickle.load(file)

Out = ["Healthy", "Consider Consultation with Doctor"]

def predict(Age, Gender, Weight, Height, Chest_Pain_Type, Heart_Rate, Systolic_BP, Diastolic_BP, Smoking, Number_of_Cigarettes_Per_Day, Diabetes, Anaemia, Past_Heart_Failures, SpO2_Level, BPM):
    # Step 2: Prepare a single entry for prediction
    # The entry is a list of features in the following order:
    # [Age, Gender, Weight, Height, Chest Pain Type, Heart Rate, Systolic BP, Diastolic BP, Smoking, 
    #  Number of Cigarettes Per Day, Diabetes, Anaemia, Any Past Heart Failures, SpO2 Level, BPM]
    single_entry = np.array([[Age, Gender, Weight, Height, Chest_Pain_Type, Heart_Rate, Systolic_BP, Diastolic_BP, Smoking, Number_of_Cigarettes_Per_Day, Diabetes, Anaemia, Past_Heart_Failures, SpO2_Level, BPM]])  # Example entry

    # Step 3: Predict the class and probabilities
    single_prediction = rf_model.predict(single_entry)
    single_prediction_proba = rf_model.predict_proba(single_entry)

    # Step 4: Print the prediction results
    print(f"Predicted class: {single_prediction[0]}")
    print(f"Prediction probabilities: {single_prediction_proba[0]}")
    accuracy = single_prediction_proba[0][0]*100
    error = single_prediction_proba[0][1]*100
    
    return (Out[single_prediction[0]], int(accuracy), int(error))


# print(predict(82, 0, 54, 149, 2, 61, 137, 96, 1, 21, 1, 1, 1, 73, 1))