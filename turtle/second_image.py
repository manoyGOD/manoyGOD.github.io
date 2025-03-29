import turtle

def create_circle(fill_color, pos_x, pos_y, size):
    turtle.penup()
    turtle.goto(pos_x, pos_y - size)
    turtle.pendown()
    turtle.color("black", fill_color)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

    turtle.width(10)
    turtle.color("black")
    turtle.circle(size)

def create_slash(pos_x, pos_y, size):
    turtle.width(30)

    # Draw blue diagonal
    turtle.color("black")
    turtle.penup()
    x1 = pos_x - size * 0.62
    y1 = pos_y + size * 0.62
    x2 = pos_x + size * 0.62
    y2 = pos_y - size * 0.62

    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)

    # Draw diagonal black border
    turtle.width(16)
    turtle.color("blue")

    # Left border
    turtle.penup()
    turtle.goto(x1 + 7, y1 - 7)
    turtle.pendown()
    turtle.goto(x2 + 7, y2 - 7)

    # Right border
    turtle.penup()
    turtle.goto(x1 - 7, y1 + 7)
    turtle.pendown()
    turtle.goto(x2 - 7, y2 + 7)

def create_no_entry(pos_x, pos_y, outer_size):
    create_circle("blue", pos_x, pos_y, outer_size)
    create_circle("white", pos_x, pos_y, outer_size * 0.65)
    create_slash(pos_x, pos_y, outer_size * 0.65)

turtle.speed(0)
create_no_entry(0, 0, 100)
turtle.hideturtle()
turtle.done()
