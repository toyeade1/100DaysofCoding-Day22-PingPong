from turtle import Turtle

UP = 0
DOWN = 180
X_POSITION = 350
Y_POSITION = 0


class PaddleGame(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1, outline=None)
        self.pu()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)