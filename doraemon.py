import turtle

def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_rectangle(color, x, y, width, height):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_doraemon():
    # Head
    draw_circle("deepskyblue", 100, 0, -100)

    # Face
    draw_circle("white", 90, 0, -90)

    # Eyes
    draw_circle("white", 20, -35, 5)
    draw_circle("white", 20, 35, 5)
    draw_circle("black", 10, -35, 15)
    draw_circle("black", 10, 35, 15)

    # Nose
    draw_circle("red", 10, 0, 10)

    # Mouth
    turtle.penup()
    turtle.goto(-40, -10)
    turtle.pendown()
    turtle.setheading(-60)
    turtle.circle(40, 120)

    # Whiskers
    turtle.penup()
    turtle.goto(-60, 0)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(40)

    turtle.penup()
    turtle.goto(-60, -10)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(40)

    turtle.penup()
    turtle.goto(-60, 10)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(40)

    # Collar
    draw_rectangle("red", -40, -40, 80, 15)

    # Bell
    draw_circle("yellow", 7, 0, -45)

    # Bell Details
    turtle.penup()
    turtle.goto(0, -48)
    turtle.pendown()
    turtle.setheading(90)
    turtle.circle(7, 180)

    turtle.hideturtle()

# Setup the turtle environment
turtle.speed(5)
turtle.bgcolor("white")

# Draw Doraemon
draw_doraemon()

# Finish drawing
turtle.done()
