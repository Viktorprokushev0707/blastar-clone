\
import pygame as pg
import random
from settings import *
from sprites import Player, Bullet # Import Player and Bullet spritesr and Bullet sprites

class Game:
    def __init__(self):
        # Initialize Pygame and create window
        pg.init()
        pg.mixer.init() # For sound
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font('arial') # Default font

    def new(self):
        # Start a new game
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.mobs = pg.sprite.Group() # Group for enemies
        self.bullets = pg.sprite.Group() # Group for player bullets
        self.player = Player()
        self.all_sprites.add(self.player)
        # !!! Placeholder: Spawn initial enemies later !!!
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        # !!! Placeholder: Add collision detection later !!!

    def events(self):
        # Game Loop - Events
        for event in pg.event.get():
            # Check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            # !!! Placeholder: Add shooting event later (e.g., spacebar) !!!
            if event.type == pg.KEYDOWN:
                 if event.key == pg.K_SPACE:
                     self.player.shoot(self.all_sprites, self.bullets)


    def draw(self):
        # Game Loop - Draw
        self.screen.fill(BLACK) # Draw background
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score), 22, WHITE, WIDTH / 2, 15)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # Game start screen
        self.screen.fill(BLACK)
        self.draw_text(TITLE, 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Arrows to move, Space to fire", 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press any key to begin", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        # Game Over/Continue screen
        if not self.running: # Don't show GO screen if user quit
             return
        self.screen.fill(BLACK)
        self.draw_text("GAME OVER", 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Score: " + str(self.score), 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press any key to play again", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS / 2) # Run slower on wait screens
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

