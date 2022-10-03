from turtle import Turtle, Screen
from Day22PongPaddle import PaddleGame
from Day22PongBall import Ball
from Day22Scoreboard import Scoreboard
import time

screen = Screen()
l_paddle = PaddleGame((-350, 0))
r_paddle = PaddleGame((350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('pong')
screen.tracer(0)


game_is_on = True

screen.listen()
screen.onkey(fun=r_paddle.up, key='Up')
screen.onkey(fun=r_paddle.down, key='Down')
screen.onkey(fun=l_paddle.up, key='w')
screen.onkey(fun=l_paddle.down, key='s')


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    scoreboard
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 330 and ball.distance(r_paddle) < 80:
        ball.bounce_x()

    elif ball.xcor() < -330 and ball.distance(l_paddle) < 80:
        ball.bounce_x()

    if ball.xcor() > 410:
        ball.ball_start_right()
        scoreboard.l_point()

    elif ball.xcor() < -410:
        ball.ball_start_left()
        scoreboard.r_point()

    if scoreboard.l_score == 10:
        print('Congratulations!! Left player wins!!')
        scoreboard.game_over()
        game_is_on = False

    elif scoreboard.r_score == 10:
        print('Congratulations!! Right player wins!!')
        scoreboard.game_over()
        game_is_on = False





screen.exitonclick()
