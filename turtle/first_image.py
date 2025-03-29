import turtle

def draw_circle():
    turtle.penup()
    turtle.goto(0, -150)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("red")
    turtle.circle(150)
    turtle.end_fill()

def draw_diamond():
    turtle.penup()
    turtle.goto(-150, 0)
    turtle.setheading(45)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("black")
    for _ in range(4):  # Corrected the for loop syntax
        turtle.forward(212)
        turtle.right(90)
    turtle.end_fill()

def draw_square():
    turtle.penup()
    turtle.goto(-75, 75)
    turtle.setheading(0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("blue")
    for _ in range(4):  # Corrected the for loop syntax
        turtle.forward(145)
        turtle.right(90)
    turtle.end_fill()

turtle.speed(5)
draw_circle()
draw_diamond()
draw_square()

turtle.hideturtle()
turtle.done()