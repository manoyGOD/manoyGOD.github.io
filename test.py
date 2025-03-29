import turtle
import math

# Function to draw a circle with a specified radius and outline width
def draw_circle(radius, outline_width, fill_color):
    turtle.pensize(outline_width)
    turtle.color("black", fill_color)
    turtle.up()
    turtle.goto(0, -radius)  # Move to starting position
    turtle.down()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

# Function to draw a diagonal bar
def draw_diagonal_bar(radius, bar_width, outline_width, fill_color):
    angle = 45  # Diagonal angle
    half_bar_width = bar_width / 2

    # Calculate corner points of the bar
    diagonal_length = radius * math.sqrt(2)
    x_offset = diagonal_length / 2 - half_bar_width
    y_offset = diagonal_length / 2 + half_bar_width

    points = [
        (-x_offset, -y_offset),
        (x_offset, -x_offset),
        (y_offset, x_offset),
        (-x_offset, y_offset)
    ]

    turtle.pensize(outline_width)
    turtle.color("black", fill_color)
    turtle.up()
    turtle.goto(points[0])
    turtle.down()
    turtle.begin_fill()

    for point in points[1:]:
        turtle.goto(point)

    turtle.goto(points[0])  # Close the shape
    turtle.end_fill()

# Initialize turtle
turtle.speed(0)
turtle.hideturtle()

# Define parameters
circle_radius = 100
outline_width = 10
bar_width = 40
fill_color = "blue"

# Draw the elements
draw_circle(circle_radius, outline_width, fill_color)
draw_diagonal_bar(circle_radius, bar_width, outline_width, fill_color)

# Finish
turtle.done()
