#BMI calc
weight = 63
height = 1.75
bmi = weight / height

if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi <= 24.9:
     print("normal")
elif bmi >= 25 and bmi <= 29.9:
   print("overweight")
elif bmi >= 30 and bmi <= 34.9:
    print("obese")
elif bmi >= 35 and bmi <= 39.9:
    print("obese")
else:
    print("morbidly obese")