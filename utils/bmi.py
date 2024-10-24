
def calculate_bmi(weight_kg, height_cm):
    """
    Calculate Body Mass Index (BMI).

    Parameters:
    weight_kg (float): Weight in kilograms.
    height_cm (float): Height in centimeters.

    Returns:
    float: Calculated BMI value and status 
    """
    height_m = int(height_cm) / 100
    weight_kg = int(weight_kg)
    if height_m <= 0:
        raise ValueError("Height must be greater than zero.")
    if weight_kg <= 0:
        raise ValueError("Weight must be greater than zero.")
    
    bmi = weight_kg / (height_m ** 2)

    if bmi < 18.5:
        status = "underweight"
    elif bmi > 18.5 and bmi < 24.9:
        status = "Normal"
    elif bmi> 24.9 and bmi < 29.9:
        status = "Overweight"
    elif bmi >= 30:
        status = "Obesity"

    return [int(bmi), status]

# Example usage:
# weight = 86  # weight in kg
# height = 172  # height in meters

# bmi_value, status = calculate_bmi(weight, height)
# print(f"The calculated BMI is: {bmi_value:.2f} {status}")
