while True:
    print("Know about yourself")
    height = float(input("Height in cm: "))
    weight = float(input("Enter your weight in kg: "))

    height_e = float(height * 0.01)

    bmi = float(weight / (height_e * height_e))
    print("BMI: " + str(bmi))

    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi < 25:
        print("Normal")
    elif 25 <= bmi < 30:
        print("Overweight")
    else:
        print("Obesity")

    retry = input("Do you want to calculate again? y / n): ").lower()
    if retry != 'y':
        break