"""Assignment 5."""

__author__ = "730494174"

import turtle

def draw_rectangle(turtle_obj, x, y, width, height, fill_color="white", outline_color="black"):
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    
    turtle_obj.color(outline_color, fill_color)
    turtle_obj.begin_fill()
    
    for _ in range(4):
        turtle_obj.forward(width if _ % 2 == 0 else height)
        turtle_obj.right(90)
    
    turtle_obj.end_fill()

def draw_circle(turtle_obj, x, y, radius, fill_color="white", outline_color="black"):
    turtle_obj.penup()
    turtle_obj.goto(x, y - radius)
    turtle_obj.pendown()
    
    turtle_obj.color(outline_color, fill_color)
    turtle_obj.begin_fill()
    
    turtle_obj.circle(radius)
    
    turtle_obj.end_fill()

def draw_line(turtle_obj, x1, y1, x2, y2, color="black"):
    turtle_obj.penup()
    turtle_obj.goto(x1, y1)
    turtle_obj.pendown()
    
    turtle_obj.color(color)
    turtle_obj.goto(x2, y2)

def draw_scene():
    # Draw two rectangles
    draw_rectangle(my_turtle, -50, 50, 80, 40)
    draw_rectangle(my_turtle, 100, -70, 120, 60, "yellow", "blue")

    # Use a loop to draw lines
    for i in range(5):
        draw_line(my_turtle, -150, -i * 30, 150, -i * 30, "red")

    # Draw a filled circle
    draw_circle(my_turtle, -30, -100, 25, "green", "purple")

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    global my_turtle
    my_turtle = turtle.Turtle()
    my_turtle.speed(2)

    draw_scene()

    turtle.done()

if __name__ == "__main__":
    main()