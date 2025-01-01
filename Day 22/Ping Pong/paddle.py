from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self, x_val, y_val):
        super().__init__()
        self.setup()
        self.setpos(x_val, y_val)


    def setup(self):
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

    def set_movement(self, screen, letter):
        from turtle import Screen
        screen = Screen()
        screen.listen()
        if letter == 'r':
            screen.onkey(fun=self.go_up, key="Up")
            screen.onkey(fun=self.go_down, key="Down")
        elif letter == 'l':
            screen.onkey(fun=self.go_up, key="w")
            screen.onkey(fun=self.go_down, key="s")

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)



