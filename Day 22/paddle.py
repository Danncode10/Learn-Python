from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_pos, y_pos, letter, screen): #Add screen as parameter
        super().__init__()
        self.screen = screen
        self.shape("square")
        self.color("white")
        #Note that a turtle starts at height=20, width=20, we need to stretch
        self.shapesize(stretch_wid=5, stretch_len=1)

        self.penup()
        self.setpos(x_pos, y_pos)

        #Define Movement
        self.movement(letter)

        #x value is used for bounce paddle of ball
        self.x_value = x_pos
        self.y_value = y_pos

    def movement(self, letter):
        if letter == 'l':
            self.screen.listen()
            self.screen.onkey(fun=self.go_up, key="w")
            self.screen.onkey(fun=self.go_down, key="s")
        elif letter == 'r':
            self.screen.listen()
            self.screen.onkey(fun=self.go_up, key="Up")
            self.screen.onkey(fun=self.go_down, key="Down")

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(x = self.xcor(), y=new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)








