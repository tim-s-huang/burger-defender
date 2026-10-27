from bullet import Bullet
import time

class BulletManager:
    def __init__(self):
        self.on_screen_bullets = []

    def shoot_bullet(self, bullet_x, bullet_y, turtle_shape):
        new_bullet = Bullet(turtle_shape)
        new_bullet.set_heading(bullet_x, bullet_y)
        self.on_screen_bullets.append(new_bullet)

    def delete_offscreen(self):
        for bullet in self.on_screen_bullets:
            if bullet.xcor() > 450 or bullet.xcor() < -450 or bullet.ycor() > 450 or bullet.ycor() < -450:
                self.on_screen_bullets.remove(bullet)

    def touching_enemy(self, fly_manager, scoreboard):
        for bullet in self.on_screen_bullets:
            for fly in fly_manager.fly_array:
                if bullet.distance(fly) < 15:
                    self.on_screen_bullets.remove(bullet)
                    bullet.ht()
                    fly_manager.fly_array.remove(fly)
                    fly.ht()
                    scoreboard.kill()


