height = float(input("Enter your height in m: \t"))
weight = float(input("Enter your weight in kg:\t"))
bmi = round(weight / height ** 2, 2)
#print(f"Your BMI is:\n{bmi}")
bmi_is = f"Your bmi is {bmi}, "
if bmi < 18.5:
    print(f"{bmi_is}you are underweight")
elif bmi < 25:
    print(f"{bmi_is}You are normal weight")
elif bmi < 30:
    print(f"{bmi_is}You are overweight")
elif bmi < 35:
    print(f"{bmi_is}You are obese")
else:
    print(f"{bmi_is}you are clinically obese")