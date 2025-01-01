from turtle import Screen
from paddle import Paddle
from ball import Ball

def main():
    screen.tracer(0) #Removes Animation, Note when using tracer, it should always manully use screen.update(), kaya naka loop dapat

    while game_on:
        screen.update()
        ball.move()
        #Collisions
        if wall_collision():
            ball.bounce_up_down_wall()
        if r_paddle_contact():
            ball.paddle_contact(pad_right.x_value, pad_right.y_value)
        if l_paddle_contact:
            ball.paddle_contact(pad_left.x_value, pad_left.y_value)


#Functions
def wall_collision():
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        return True
    else:
        return False

def r_paddle_contact():
    # if ball.distance(pad_right) < 50 and ball.xcor() == 340:
    #     print("Made Contact")
    if ball.xcor() >= 350 and ball.xcor() <= 360:
        return True
    else:
        return False

def l_paddle_contact():
    # if ball.distance(pad_right) < 50 and ball.xcor() == 340:
    #     print("Made Contact")
    if ball.xcor() <= -380:
        return True
    else:
        return False



#Global Variables
screen = Screen()
game_on = True
ball = Ball()
pad_right = Paddle(350, 0, 'r', screen)
pad_left = Paddle(-350, 0, 'l', screen)


#Screen Set up
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong Game")

#CALL
main()
screen.mainloop()