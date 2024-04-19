weight = float(input("Enter weight (in kgs): "))
height = float(input("Enter height (in meters): "))

bmi = weight / (height ** 2)

print("BMI:", bmi)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Pre-Obese")
elif bmi < 35:
    print("Obese Class I")
elif bmi < 40:
    print("Obese Class II")
else:
    print("Obese Class III")
