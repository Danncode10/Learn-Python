from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


def main():
    while game_on:
        screen.update()
        ball.move()
        ball.detect_collision(r_pad, l_pad)
        scoring()
        ball.detect_miss_ball()

#Global Variables
screen = Screen()
r_pad = Paddle(350, 0)
l_pad = Paddle(-350, 0)
game_on = True
ball = Ball()
l_score = Scoreboard(-100, 240)
r_score = Scoreboard(100, 240)

#Functions
def set_up_screen():
    global screen
    screen.tracer(0)
    screen.setup(height=600, width=800)
    screen.bgcolor("black")
    screen.title("Ping Pong")

def paddle_movement():
    global r_pad, l_pad
    r_pad.set_movement(screen, 'r')
    l_pad.set_movement(screen, 'l')

def scoring():
    print("Scoring function called!")
    global l_score, r_score
    if ball.xcor() > 380:
        l_score.score += 1
        l_score.show_score()
    elif ball.xcor() < -380:
        r_score.score += 1
        r_score.show_score()

#Call
set_up_screen()
paddle_movement()
main()
screen.mainloop()