from turtle import Turtle, Screen, Shape
from bullet_manager import BulletManager
from burger import Burger
from fly_manager import FlyManager
from score_manager import ScoreManager
import time
from tkinter import PhotoImage

START_FLY_SPAWN_RATE = 100

my_screen = Screen()
my_screen.screensize(800,600)
my_screen.title("Burger Defender")
my_screen.tracer(0)
my_screen.bgpic("cloth_bg.gif")

# Add Sprites
BURGER_IMAGE = PhotoImage(file="burger.gif").subsample(2, 2)
my_screen.addshape("burger", Shape("image", BURGER_IMAGE))

SEED_IMAGE = PhotoImage(file="seed.gif").subsample(70, 70)
my_screen.addshape("seed", Shape("image", SEED_IMAGE))

FLY_IMAGE = PhotoImage(file="fly.gif").subsample(3, 3)
my_screen.addshape("fly", Shape("image", FLY_IMAGE))

HEAL_FLY_IMAGE = PhotoImage(file="heal_fly.gif").subsample(3, 3)
my_screen.addshape("heal_fly", Shape("image", HEAL_FLY_IMAGE))

bullet_manager = BulletManager()
player = Burger("burger")
fly_manager = FlyManager()
score_board = ScoreManager()

# Shoot bullet on click
def shoot_bullet(x, y):
    bullet_manager.shoot_bullet(x, y, "seed")

my_screen.onclick(shoot_bullet)

fly_timer = 0
spawn_counter = 0

game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.01)

    # Check collisions
    fly_manager.touching_player(player, score_board)
    bullet_manager.touching_enemy(fly_manager, score_board)

    # Update scoreboard
    score_board.update_scores(player.lives)

    # Bullets move forward
    for bullet in bullet_manager.on_screen_bullets:
        bullet.move_forward()

    # Flies move towards player
    for fly in fly_manager.fly_array:
        fly.go_to_player()

    # Increase Fly Spawn Rate
    if spawn_counter == 10 and START_FLY_SPAWN_RATE > 20:
        START_FLY_SPAWN_RATE -= 10
        spawn_counter = 0
        fly_timer += 1

    # Spawn Fly
    if fly_timer == START_FLY_SPAWN_RATE:
        fly_manager.spawn_fly("fly", "heal_fly")
        spawn_counter += 1
        fly_timer = 0
    else:
        fly_timer += 1

    # Check for Game Over
    if player.lives == 0:
        game_is_on = False


# Game Over
score_board.game_over()
if score_board.score > score_board.high_score:
    score_board.set_high_score()

my_screen.mainloop()
