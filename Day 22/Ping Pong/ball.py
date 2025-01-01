from select import select
from turtle import Turtle
import random
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.setup()
        self.angle = 45


    def setup(self):
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.color("white")

    def move(self):
        self.setheading(self.angle)
        self.forward(10)
        time.sleep(0.05)

    def detect_collision(self, pad_r, pad_l):
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.up_down_wall_collision()

        # ------- Paddle collision
        elif (self.xcor() >= 330 and self.distance(pad_r) < 50):
            #sometimes nag vivibrate, solution, subtract coordinate of x
            self.setx(self.xcor() - 5)
            self.paddle_collision()
        elif (self.xcor() <= -330 and self.distance(pad_l) < 50):
            #sa paddle left, dapat mag add 5, hindi subract kase nasa negative coordinates
            self.setx(self.xcor() + 5)
            self.paddle_collision()

    def up_down_wall_collision(self):
        self.angle *= -1

    def paddle_collision(self):
        self.angle = 180 - self.angle

    def detect_miss_ball(self):
        self.detect_right_miss()
        self.detect_left_miss()

    def detect_right_miss(self):
        if self.xcor() > 380:
            self.reset_position()
            self.angle = random.randint(135, 225)

    def detect_left_miss(self):
        if self.xcor() < -380:
            self.reset_position()
            self.angle = random.randint(-45, 45)

    def reset_position(self):
        self.hideturtle()
        self.goto(0,0)
        self.showturtle()
        # self.angle = 180 - self.angle





