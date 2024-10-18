year = int(input("Enter Your Age: "))

days = (90*365) - (365*year)
weeks = (90*52) - (52*year)
months = (90*12) - (12*year)

print(f"You have {days} days remaining, {weeks} weeks, and {months} months left.")