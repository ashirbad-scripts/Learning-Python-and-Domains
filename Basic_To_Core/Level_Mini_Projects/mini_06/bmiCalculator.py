def calculateBMI():
    try:
        w = float(input("Enter weight in kg: "))
        h = float(input("Enter height in meters: "))
        bmi = w / (h ** 2)
        print(f"Your BMI is : {bmi:.2f}")

        if bmi < 18.5:
            print("Underweight")
        elif bmi >= 18.5 and bmi <= 30:
            print("Normal")
        else:
            print("overweight")
        
    except ValueError as err:
        print(f"Error message: {err}")
        return None

result = calculateBMI()

