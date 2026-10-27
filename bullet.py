"""
1. Small Seed Sprite - DONE
2. Move in direction clicked - DONE
3. Disappear if off-screen
4. Damage enemy if hit
5. Add sprite
"""
from turtle import Turtle
import math

BULLET_OFFSET = 50

class Bullet(Turtle):
    def __init__(self, turtle_shape):
        super().__init__()
        self.shape(turtle_shape)
        self.speed("fastest")
        self.pu()
        self.goto(0, 0)

    def move_forward(self):
        self.forward(10)

    def set_heading(self, x, y):
        heading_radians = math.atan2(y, x)
        heading_angle = round(heading_radians * (180 / math.pi))
        self.setheading(heading_angle)
        self.forward(90)

