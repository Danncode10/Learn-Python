from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball_setup()
        self.angle = 60 #for walls in y axis contact

    def ball_setup(self):
        self.shape("circle")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.penup()
        self.color("white")

    def move(self):
        # new_x = self.xcor() + 10
        # new_y = self.ycor() + 10
        # self.goto(new_x, new_y)
        time.sleep(0.1)
        self.setheading(self.angle)
        self.forward(10)

    def bounce_up_down_wall(self):
        self.angle *= -1 #Inverse of angle

    def paddle_contact(self, x_val, y_val): #x_val and y_val are paddle values
        if(x_val == self.xcor() and self.distance(y_val) <= 50):
            self.angle = 180 - self.angle

        # self.angle = 180 - self.angle

