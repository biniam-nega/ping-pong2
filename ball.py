import turtle
import time
import threading


class Ball:
    def __init__(self, speed, paddle_left, paddle_right, score):
        self.ball = turtle.Turtle()
        self.dx = speed
        self.dy = speed
        self.pr = paddle_right
        self.pl = paddle_left
        self.pen = score
        self.thread = threading.Thread(target=self.speedup)
        self.init_ball()

    def init_ball(self):
        self.ball.penup()
        self.ball.speed(0)
        self.ball.shape('circle')
        self.ball.color('white')
        self.ball.goto(0, 0)
        self.thread.start()

    def update(self):
        self.ball.setx(self.ball.xcor() + self.dx)
        self.ball.sety(self.ball.ycor() + self.dy)
        self.check_collision()

    def check_collision(self):
        self.check_wall_collision()
        self.check_paddle_collision()

    def check_wall_collision(self):
        if self.ball.ycor() >= 290:
            self.ball.sety(290)
            self.dy *= -1
        elif self.ball.ycor() <= -280:
            self.ball.sety(-280)
            self.dy *= -1

        if self.ball.xcor() >= 380:
            self.ball.goto(0, 0)
            time.sleep(1)
            self.dx *= -1
            self.pl.score += 1
            self.update_score()
        elif self.ball.xcor() <= -390:
            self.ball.goto(0, 0)
            time.sleep(1)
            self.dx *= -1
            self.pr.score += 1
            self.update_score()

    def check_paddle_collision(self):
        if (330 < self.ball.xcor() < 350) and \
                (self.pr.paddle.ycor() + 50 > self.ball.ycor() > self.pr.paddle.ycor() - 50):
            self.dx *= -1
        if (-330 > self.ball.xcor() > -350) and \
                (self.pl.paddle.ycor() + 50 > self.ball.ycor() > self.pl.paddle.ycor() - 50):
            self.dx *= -1

    def update_score(self):
        self.pen.pen.clear()
        self.pen.pen.write('Player A: ' + str(self.pl.score) + '  Player B: ' + str(self.pr.score), align='center',
                       font=('Courier', 12, 'normal'))

    def speedup(self):
        while True:
            time.sleep(10)
            self.dx += 0.1 if self.dx > 0 else -0.1
            self.dy += 0.1 if self.dy > 0 else -0.1
            print('speeding up: dx({}) dy({})'.format(self.dx, self.dy))

    def reset_ball(self):
        self.dx = 0.3
        self.dy = 0.3
        self.ball.goto(0, 0)
