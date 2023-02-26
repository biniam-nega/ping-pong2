import turtle


class Paddle:
    def __init__(self, position, keys, win):
        self.position = position
        self.keys = keys
        self.paddle = turtle.Turtle()
        self.window = win
        self.score = 0
        self.init_paddle()

    def init_paddle(self):
        self.paddle.color("white")
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.speed(0)
        self.paddle.penup()
        self.paddle.goto(self.position, 0)
        self.bind_keys()

    def bind_keys(self):
        self.window.onkeypress(self.move_up, self.keys[0])
        self.window.onkeypress(self.move_down, self.keys[1])

    def move_up(self):
        y = self.paddle.ycor()
        if y < 250:
            y += 20
            self.paddle.sety(y)

    def move_down(self):
        y = self.paddle.ycor()
        if y > -250:
            y -= 20
            self.paddle.sety(y)
