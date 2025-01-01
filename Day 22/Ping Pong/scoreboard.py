from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")

class Scoreboard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.score = 0
        self.x = x
        self.y = y
        self.setup()

    def setup(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(self.x, self.y)
        self.show_score()

    def show_score(self):
        self.clear()  # Clear previous score
        self.write(self.score, align=ALIGNMENT, font=FONT)
