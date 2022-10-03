from turtle import Turtle
import time

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color('white')
        self.pu()
        # self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.08

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def ball_start_right(self):
        self.goto(0, 0)
        self.move_speed = 0.08
        self.bounce_x()

    def ball_start_left(self):
        self.goto(0, 0)
        self.move_speed = 0.08
        self.bounce_x()




