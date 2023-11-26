def calculate_bmi(weight, height):
    """
    Calculate BMI (Body Mass Index).
    Formula: BMI = weight (kg) / (height (m) ^ 2)
    """
    if weight <= 0 or height <= 0:
        return "Invalid input. Weight and height must be positive numbers."

    # Convert height from centimeters to meters
    height_in_meters = height / 100.0

    # Calculate BMI
    bmi = weight / (height_in_meters ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Interpret BMI value and provide a general health category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    # Get user input
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in centimeters: "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Interpret BMI
    category = interpret_bmi(bmi)

    # Display the result
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()
