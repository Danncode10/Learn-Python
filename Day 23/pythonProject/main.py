import turtle
from car import Car

# Main program
if __name__ == "__main__":
    # Screen setup
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Custom Turtle Shape Example")

    # Create a Car object with custom shape
    my_car = Car()  # Use default shape "car_image.gif"

    # Move the car around

    # Keep the window open
    screen.mainloop()
