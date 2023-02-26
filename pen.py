import turtle


class Pen:
    def __init__(self, text):
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        self.pen.write(text, align='center', font=('Courier', 12, 'normal'))
