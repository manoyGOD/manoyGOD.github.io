import turtle

def draw_circle():
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.color("black", "blue")
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()

def draw_diagonal_line():
    turtle.penup()
    turtle.goto(-70, 70)
    turtle.pendown()
    turtle.color("black")
    turtle.width(10)
    turtle.goto(70, -70)

def main():
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    turtle.speed(3)
    draw_circle()
    draw_diagonal_line()
    turtle.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
