import turtle
import sys

import paddle as pd
import ball as bl
import pen as pn


def start_game():
    global game_on, pen
    pen.pen.clear()
    if game_on:
        pen.pen.clear()
        pen.pen.write('Press Space to start game', align='center', font=('Courier', 12, 'normal'))
        ball.reset_ball()
    else:
        pen.pen.clear()
        pen.pen.write('Player A: 0  Player B: 0', align='center', font=('Courier', 12, 'normal'))
        ball.reset_ball()
    game_on = not game_on


wn = turtle.Screen()
wn.title('Ping pong by Biniam')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

# pen
pen = pn.Pen('Press Space to start game')

wn.listen()
wn.onkeypress(start_game, 'space')
# Paddle left
paddle_left = pd.Paddle(-350, ('w', 's'), wn)
# Paddle right
paddle_right = pd.Paddle(350, ('Up', 'Down'), wn)
# Ball
ball = bl.Ball(0.1, paddle_left, paddle_right, pen)
# game status flag
game_on = False

# Main game loop
while True:
    wn.update()
    if game_on:
        ball.update()
