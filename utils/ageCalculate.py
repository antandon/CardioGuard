from datetime import datetime

def calculate_age(dob_str):
    """
    Calculate the age based on the date of birth.

    Parameters:
    dob_str (str): Date of birth in the format 'YYYY-MM-DD'.

    Returns:
    int: Current age.
    """
    # Convert the input string to a datetime object
    dob = datetime.strptime(dob_str, '%Y-%m-%d')
    
    # Get the current date
    today = datetime.today()
    
    # Calculate the age
    age = today.year - dob.year
    
    # Adjust age if the birthday has not occurred yet this year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1

    return age

# Example usage:
# dob_input = '1994-05-15'  # Example date of birth
# age = calculate_age(dob_input)
# print(f"Current age: {age} years")
