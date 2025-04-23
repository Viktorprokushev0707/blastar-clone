\
import pygame as pg
from settings import *

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        # Draw player ship (triangle)
        self.image = pg.Surface((30, 40)) # Smaller surface
        self.image.fill(BLACK) # Fill with background color first
        # Define points for the triangle (pointing up)
        ship_points = [(15, 0), (0, 40), (30, 40)]
        pg.draw.polygon(self.image, WHITE, ship_points)
        self.image.set_colorkey(BLACK) # Make black transparent
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.speedx = -PLAYER_SPEED
        if keystate[pg.K_RIGHT]:
            self.speedx = PLAYER_SPEED
        self.rect.x += self.speedx

        # Keep player on screen
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self, all_sprites_group, bullets_group):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites_group.add(bullet)
        bullets_group.add(bullet)

# Add other sprite classes (Enemy, Bullet, Explosion etc.) later
# Bullet class
class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        # !!! Placeholder: Replace with actual bullet image later !!!
        self.image = pg.Surface((5, 10))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10 # Negative value means moving up

    def update(self):
        self.rect.y += self.speedy
        # Kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()
# Bullet class
class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        # !!! Placeholder: Replace with actual bullet image later !!!
        self.image = pg.Surface((5, 10))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10 # Negative value means moving up

    def update(self):
        self.rect.y += self.speedy
        # Kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()
