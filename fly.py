"""
1. Small fly sprite
2. Spawn at random location
3. Move towards burger
4. Disappear if hit with bullet
5. Disappear if contact burger
6. Increase spawn rate over time
7. Add sprite
"""

from turtle import Turtle
import random
import math

X_SPAWN = 650
Y_SPAWN = 550
MOVE_SPEED = 2
SIDES = ["left", "right", "top", "bottom"]

class Fly(Turtle):
    def __init__(self, turtle_shape):
        super().__init__()
        self.shape(turtle_shape)
        self.pu()
        self.random_spawn(random.choice(SIDES))
        self.name = "normal"

    def move_to_spawn(self, x, y):
        self.goto(x, y)
        heading_radians = math.atan2(y, x)
        heading_angle = round(heading_radians * (180 / math.pi))
        self.setheading(heading_angle)

    def random_spawn(self, side):
        if side == "left":
            x_spawn = -X_SPAWN
            y_spawn = random.randint(-Y_SPAWN, Y_SPAWN)
        elif side == "right":
            x_spawn = X_SPAWN
            y_spawn = random.randint(-Y_SPAWN, Y_SPAWN)
        elif side == "top":
            x_spawn = random.randint(-X_SPAWN, X_SPAWN)
            y_spawn = Y_SPAWN
        else:
            x_spawn = random.randint(-X_SPAWN, X_SPAWN)
            y_spawn = -Y_SPAWN

        self.move_to_spawn(x_spawn, y_spawn)

    def go_to_player(self):
        self.backward(2)






