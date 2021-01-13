# Simple Pong game
import turtle

# Creating a window/screen for a game
window = turtle.Screen()
window.title("Pong by Petar")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

#Score
score_left = 0
score_right = 0

# Left Paddle
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape("square")
paddle_left.color("white")
paddle_left.shapesize(stretch_len=1, stretch_wid=5)
paddle_left.penup()
paddle_left.goto(-350, 0)

# Right Paddle
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape("square")
paddle_right.color("white")
paddle_right.shapesize(stretch_len=1, stretch_wid=5)
paddle_right.penup()
paddle_right.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.07
ball.dy = -0.07


# Functions for moving paddles
def paddle_left_up():
    y = paddle_left.ycor()
    y += 20
    paddle_left.sety(y)

# Scoreboard
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write("Player Left: 0   Player Right: 0", align="center", font=("Courier", 24, "normal"))

def paddle_left_down():
    y = paddle_left.ycor()
    y -= 20
    paddle_left.sety(y)


def paddle_right_up():
    y = paddle_right.ycor()
    y += 20
    paddle_right.sety(y)


def paddle_right_down():
    y = paddle_right.ycor()
    y -= 20
    paddle_right.sety(y)

# Keyboard binding


window.listen()
window.onkeypress(paddle_left_up, "w")
window.onkeypress(paddle_left_down, "s")
window.onkeypress(paddle_right_up, "Up")
window.onkeypress(paddle_right_down, "Down")

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # reverse the direction of the ball

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1  # reverse the direction of the ball

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_left += 1
        scoreboard.clear()
        scoreboard.write(f"Player Left: {score_left}   Player Right: {score_right}", align="center",
                         font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_right += 1
        scoreboard.clear()
        scoreboard.write("Player Left: {}   Player Right: {}".format(score_left, score_right), align="center",
                         font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_right.ycor() + 40 and ball.ycor() > paddle_right.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_left.ycor() + 40 and ball.ycor() > paddle_left.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
