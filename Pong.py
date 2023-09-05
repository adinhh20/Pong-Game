import turtle  # to create pictures & shapes with a virtual canvas
from time import sleep  # to execute sleep(time delay) function
import random

wm = turtle.Screen()
wm.title("Pong by AnhD")
wm.bgcolor("black")
wm.setup(width=800, height=600)
wm.tracer(0)

# Score
score_l = 0
score_r = 0

# Paddle L
paddle_l = turtle.Turtle()  # create turtle object
paddle_l.speed(0)           # max speed of animation
paddle_l.shape("square")    # shape with 20x20 pixels defaut size
paddle_l.color("white")
paddle_l.shapesize(stretch_wid=5, stretch_len=1)    # 20x100
paddle_l.penup()            # move turtle without leaving tracks
# pendown is moving turtle with leaving tracks
paddle_l.goto(-350, 0)      # starting position


# Paddle R
paddle_r = turtle.Turtle()
paddle_r.speed(0)
paddle_r.shape("square")
paddle_r.color("white")
paddle_r.shapesize(stretch_wid=5, stretch_len=1)
paddle_r.penup()
paddle_r.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
# move diagonally
ball.dx = random.choice([-2, 2])   # d = delta/change
# depending on computers, these values can be changed
ball.dy = random.choice([-2, 2])


# Pen - for displaying score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player L: {}  Player R: {}".format(score_l, score_r), align="center",
          font=("Courier", 24, "normal"))

# Function


def paddle_l_up():          # def = define function
    y = paddle_l.ycor()     # return y coordinate/value y
    y += 20                 # add 20 pixels
    paddle_l.sety(y)        # set position


def paddle_l_down():
    y = paddle_l.ycor()
    y -= 20
    paddle_l.sety(y)


def paddle_r_up():
    y = paddle_r.ycor()
    y += 20
    paddle_r.sety(y)


def paddle_r_down():
    y = paddle_r.ycor()
    y -= 20
    paddle_r.sety(y)


# Keyboard binding
wm.listen()     # call the function to listen to the keyboard
wm.onkeypress(paddle_l_up, "w")
wm.onkeypress(paddle_l_down, "s")
wm.onkeypress(paddle_r_up, "Up")        # "Up" for top arrow key
wm.onkeypress(paddle_r_down, "Down")

# Main Game Loop
while True:
    sleep(0.01)     # delay your code so that the loop can update
    wm.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking - to not let things get out of the canvas
    if ball.ycor() > 290:
        # 290 = 600/2 - 10 (divide height then minus half length)
        ball.sety(290)  # set position then
        ball.dy *= -1   # reverse direction

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        # 390 = 400/2 - 10 (divide length then minus half length)
        # go back to starting point once it hits the right side
        ball.goto(0, 0)
        ball.dx *= -1
        score_l += 1
        pen.clear()
        pen.write("Player L: {}  Player R: {}".format(score_l, score_r), align="center",
                  font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_r += 1
        pen.clear()
        pen.write("Player L: {}  Player R: {}".format(score_l, score_r), align="center",
                  font=("Courier", 24, "normal"))

    # Paddle & Ball Collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_r.ycor() + 40 and ball.ycor() > paddle_r.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_l.ycor() + 40 and ball.ycor() > paddle_l.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
