"""
1. Sit in middle of screen as burger - DONE
2. Shoot in direction clicked - DONE
3. Take damage if hit
4. Lose game if dead
5. Add sprite
"""

from turtle import Turtle

class Burger(Turtle):
    def __init__(self, turtle_shape):
        super().__init__()
        self.shape(turtle_shape)
        self.pu()
        self.goto(0, 0)
        self.lives = 5

    def take_damage(self):
        self.lives -= 1

    def gain_health(self):
        self.lives += 1



