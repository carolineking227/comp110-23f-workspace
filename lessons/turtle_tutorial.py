from turtle import Turtle, colormode
colormode(255)
leo: Turtle = Turtle()
bob: Turtle = Turtle()

"""Describe leo's attibutes and center leo!"""
leo.color(57, 44, 91)
leo.penup()
leo.goto(0, 0)
leo.pendown()
leo.speed(50)

"""Draw the triangle while filling it in!"""
leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()

"""Describe bob's attributes and center bob!"""
bob.color(47, 28, 87)
bob.penup()
bob.goto(0, 0)
bob.pendown()
bob.speed(70)

"""Have bob draw an outline for the triangle without filling it in!"""
side_length: int = 300
i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(120)
    i = i + 1

""""Have bob draw another outline for a slightly different triangle!"""
side_length = side_length * 0.97
i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(121)
    i = i + 1