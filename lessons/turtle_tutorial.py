from turtle import Turtle, colormode, done

# Setting up the turtle
leo: Turtle = Turtle()

# Exercise One: Draw a square
for _ in range(4):
    leo.forward(300)
    leo.left(90)

# Simplifying with Loops
i: int = 0
while i < 3:
    leo.forward(300)
    leo.left(120)
    i += 1

# GoTo, Penup, and Pendown
leo.penup()
leo.goto(45, 60)
leo.pendown()

# Exercise Two: Draw a triangle
i = 0
while i < 3:
    leo.forward(300)
    leo.left(120)
    i += 1

# Pen Color
leo.color("blue")

# Fill Color
leo.begin_fill()
i = 0
while i < 3:
    leo.forward(300)
    leo.left(120)
    i += 1
leo.end_fill()

# Other Useful Color Commands
leo.pencolor("pink")
leo.fillcolor(32, 67, 93)
leo.color("green", "yellow")

# Exercise Three: Color Picker values
# Try different RGB values for colors

# Speed, Visibility, and the Fun Part
leo.speed(50)
leo.hideturtle()

# Mini-Project
bob: Turtle = Turtle()

# Setting up Bob
bob.color("black")
bob.penup()
bob.goto(45, 60)
bob.pendown()
bob.speed(50)

# Create an outline of Leo's filled-in triangle
side_length: int = 300
for _ in range(3):
    bob.forward(side_length)
    bob.left(120)

# Duplicate the code for more linework
for _ in range(200):  # Experiment with the number of loops
    bob.forward(side_length)
    bob.left(120.5)  # Experiment with the angle
    side_length = side_length * 0.97

done()