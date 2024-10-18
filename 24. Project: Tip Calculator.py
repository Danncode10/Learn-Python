print("Welcome to the tip Calculator")
bill = float(input("What was the total Bill: "))

percent = float(input("What percentage tip would you like to give? 10, 12, or 15? "))/100

people = int(input("How many people to split the bill? "))

tip = (bill*percent)+bill
tip = round((tip/people),2)

print(f"Each Person Should Pay: {tip}")


