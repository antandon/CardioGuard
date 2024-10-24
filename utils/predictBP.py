import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Example dataset (replace with your actual data)
# X should be a numpy array or pandas DataFrame with SpO2 and PR as features
# y_systolic should be a numpy array or pandas Series with systolic BP values

X = np.array([[98, 75], [95, 80], [92, 85]])
y_systolic = np.array([120, 130, 115])

# Split the data into training and testing sets
X_train, X_test, y_systolic_train, y_systolic_test = train_test_split(X, y_systolic, test_size=0.2, random_state=42)

# Initialize the linear regression model for systolic BP
model_systolic = LinearRegression()

# Train the model
model_systolic.fit(X_train, y_systolic_train)

# Predict on the test set
y_systolic_pred = model_systolic.predict(X_test)

# Evaluate the model (example using mean squared error)
mse_systolic = mean_squared_error(y_systolic_test, y_systolic_pred)
# print(f"Mean Squared Error (Systolic BP): {mse_systolic}")

def getSystolicBloodPressure(spo2=98, pulse_rate=75):
    new_data = np.array([[spo2, pulse_rate]])  # Replace with actual SpO2 and PR values
    predicted_systolic = model_systolic.predict(new_data.reshape(1, -1))
    # print(f"Predicted Systolic BP for new data: {int(predicted_systolic[0])}")
    thr = ((spo2 + pulse_rate + mse_systolic/10)/3)*0.70

    predicted_dystolicBP = predicted_systolic[0] - thr
    return [int(predicted_systolic[0]), int(predicted_dystolicBP)]


# print(getSystolicBloodPressure())