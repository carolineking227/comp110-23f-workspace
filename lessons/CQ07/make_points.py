"""Make_points portion of the lesson!"""

from lessons.CQ07.point import Point

"""Create a new Point!"""
p1 = Point(3.0, 4.0)

"""Test the scale_by method!"""
p1.scale_by(2)
print(f"Point p1 after scaling by 2: ({p1.x}, {p1.y})")

"""Test the scale method!"""
p2 = p1.scale(3)
print(f"New Point p2 after scaling p1 by 3: ({p2.x}, {p2.y})")