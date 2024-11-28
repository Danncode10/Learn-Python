from operator import truediv

from dictionary_coffee import menu
from dictionary_coffee import resources
from dictionary_coffee import coin

money = 0


def enterChoice():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice in ["espresso", "latte", "cappuccino", "report", "off"]:
            return choice
        else:
            print("Invalid Input")


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:.2f}")


def checkResources(choice):
    """Check if enough resources are available to make the selected drink."""
    for ingredient, amount in menu[choice]["ingredients"].items():
        if amount > resources.get(ingredient, 0):
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


def processResources(choice):
    """Deduct the resources required for the selected drink."""
    global money
    for ingredient, amount in menu[choice]["ingredients"].items():
        resources[ingredient] -= amount
    money += menu[choice]["cost"]


def processCoin(choice):
    """Process the coin input and return if enough money was provided."""
    price_of_coffee = menu[choice]['cost']
    print(f"The cost of the coffee is ${price_of_coffee:.2f}")

    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total_amount = quarters + dimes + nickels + pennies

    if total_amount < price_of_coffee:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        change = total_amount - price_of_coffee
        print(f"Here is ${change:.2f} in change")
        return True


# ----------- MAIN PROGRAM -----------

running = True
while running:
    choice = enterChoice()
    if choice == "report":
        report()
    elif choice == "off":
        running = False
        print("Turning off the machine.")
    else:
        # Check if resources are sufficient for the selected drink
        if checkResources(choice):
            # Process payment
            if processCoin(choice):
                # Deduct resources if payment is successful
                processResources(choice)
                print(f"Here is your {choice}. Enjoy!")