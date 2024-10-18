mass = int(input("Enter Your weight in kg: "))
height = float(input("Enter Your Height in meters: "))

bmi = round(mass/(height*height),2)
print("Your BMI is " + str(bmi))