from fly import Fly
from heal_fly import HealFly
import random

FLY_HIT_OFFSET = 80

class FlyManager:
    def __init__(self):
        self.fly_array = []

    def spawn_fly(self, turtle_shape, turtle_shape_heal):
        heal_spawn_odd = random.randint(1, 15)
        if heal_spawn_odd == 12:
            new_fly = HealFly(turtle_shape_heal)
        else:
            new_fly = Fly(turtle_shape)
        self.fly_array.append(new_fly)

    def touching_player(self, player, scoreboard):
        for fly in self.fly_array:
            if fly.distance(player) < FLY_HIT_OFFSET:
                fly.reset()
                fly.ht()
                self.fly_array.remove(fly)
                if fly.name == "normal":
                    player.take_damage()
                    scoreboard.hit()
                else:
                    if player.lives < 5:
                        player.gain_health()
                    scoreboard.life_up()