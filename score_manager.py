"""
1. Display Lives left
2. Display Points
3. Display High Score
"""

FONT_TUPLE = ("Calibre", 36, "normal")
TEXT_OFFSET = 460

from turtle import Turtle

class ScoreManager(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.ht()
        self.pu()
        self.get_high_score()
        self.update_scores(5)

    def update_scores(self, health):
        self.clear()
        self.write_score()
        self.write_health(health)
        self.write_high_score()

    def write_score(self):
        self.goto(-TEXT_OFFSET + 40, TEXT_OFFSET)
        self.write(f"Current Score: {self.score}", align="center", font=FONT_TUPLE)

    def write_health(self, health):
        self.goto(TEXT_OFFSET + 40, TEXT_OFFSET)
        self.write(f"Lives: {health}", align="center", font=FONT_TUPLE)

    def write_high_score(self):
        self.goto(-TEXT_OFFSET + 40, -TEXT_OFFSET)
        self.write(f"High Score: {self.high_score}", align="center", font=FONT_TUPLE)

    def hit(self):
        self.score -= 50
        if self.score < 0:
            self.score = 0

    def kill(self):
        self.score += 10

    def life_up(self):
        self.score += 50

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align="center", font=("Calibre", 60, "normal"))

    def get_high_score(self):
        with open("high_score.txt") as file:
            high_score_file = file.readlines()
            self.high_score = int(high_score_file[0])
        file.close()

    def set_high_score(self):
        with open("high_score.txt", mode='w') as file:
            file.write(str(self.score))
        file.close()

        self.high_score = self.score
        self.update_scores("DEAD!")




