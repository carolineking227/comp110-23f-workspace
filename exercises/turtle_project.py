"""Ex05 - create an art scene drawn by a turtle."""

from turtle import Turtle, Screen, colormode, done
import random


def main() -> None:
    """The entrypoint of the scene."""
    colormode(255)

    leo: Turtle = Turtle()
    leo.speed(2)

    # Draw repeating elements
    for _ in range(3):
        draw_random(leo)

    done()


def draw_random(a_turtle: Turtle) -> None:
    """Draw a random element in a random place."""
    x, y = random.uniform(-200, 200), random.uniform(-200, 200)

    if random.choice([True, False]):
        draw_tree(a_turtle, x, y)
    else:
        draw_house(a_turtle, x, y)


def draw_tree(a_turtle: Turtle, x: float, y: float) -> None:
    """Draw a tree."""
    draw_trunk(a_turtle, x, y)
    draw_leaves(a_turtle, x, y + 20)


def draw_trunk(a_turtle: Turtle, x: float, y: float) -> None:
    """Draw a tree trunk."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()

    a_turtle.color("brown")
    a_turtle.begin_fill()
    for _ in range(2):
        a_turtle.forward(20)
        a_turtle.left(90)
    a_turtle.end_fill()


def draw_leaves(a_turtle: Turtle, x: float, y: float) -> None:
    """Draw tree leaves."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()

    a_turtle.color("green")
    a_turtle.begin_fill()
    a_turtle.circle(30)
    a_turtle.end_fill()


def draw_house(a_turtle: Turtle, x: float, y: float) -> None:
    """Draw a house at the given position."""
    draw_house_body(a_turtle, x, y)
    draw_roof(a_turtle, x, y + 20)


def draw_house_body(a_turtle: Turtle, x: float, y: float) -> None:
    """Draw the body of the house."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()

    a_turtle.color("blue")
    a_turtle.begin_fill()
    for _ in range(4):
        a_turtle.forward(40)
        a_turtle.left(90)
    a_turtle.end_fill()


def draw_roof(a_turtle: Turtle, x: float, y: float) -> None:
    """Draw the roof of the house."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()

    a_turtle.color("red")
    a_turtle.begin_fill()
    for _ in range(3):
        a_turtle.forward(40)
        a_turtle.left(120)
    a_turtle.end_fill()


class TurtleScreenSetup:
    """A simple class to set up the turtle screen."""
    def __init__(self) -> None:
        """Define init values of the screen."""
        self.screen = Screen()
        self.screen.bgcolor("skyblue")
        self.screen.title("Repeating Elements Scene")


if __name__ == "__main__":
    main()