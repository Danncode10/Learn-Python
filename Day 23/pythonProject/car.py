import turtle
import os


class Car(turtle.Turtle):
    def __init__(self, shape_name="car_image.gif"):
        super().__init__()

        # Dynamically get the full path to the image file
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of this script
        shape_path = os.path.join(script_dir, shape_name)

        # Register the custom shape
        screen = turtle.Screen()
        if os.path.exists(shape_path):
            screen.register_shape(shape_path)
            self.shape(shape_path)
        else:
            raise FileNotFoundError(f"Shape file '{shape_path}' not found!")

        # Optional: Prevent drawing while moving
        self.penup()
        self.speed(1)
        self.set_movement()

    def set_movement(self):
        self.screen.listen()
        self.screen.onkey(fun=self.move_up, key="Up")
        self.screen.onkey(fun=self.move_down, key="Down")
        self.screen.onkey(fun=self.move_left, key="Left")
        self.screen.onkey(fun=self.move_right, key="Right")

    def move_up(self):
        self.setheading(90)
        self.forward(10)

    def move_down(self):
        self.setheading(270)
        self.forward(10)

    def move_left(self):
        self.setheading(180)
        self.forward(10)

    def move_right(self):
        self.setheading(0)
        self.forward(10)

