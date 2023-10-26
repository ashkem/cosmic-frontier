"""
Main script for running the game.
   This script initializes a simple game using the Pygame module. 
   The game involves controlling a player that shoots lasers to destroy meteors in space. 
   The player has a shield that diminishes when coming into contact with meteors. 
   The game ends when the player's shield reaches zero. 
   During the game, laser shot and explosion sounds are played, as well as background music. 
   The script also includes start and game-over interfaces, along with a scoring function that 
   tracks the number of destroyed meteors. The game runs in a main loop that controls game logic, 
   event detection, and rendering of elements on the screen.
"""

import pygame
from config import setting
from app.controller.meteor_controller import MeteorController
from app.controller.player_controler import PlayerControler
from app.controller.life_controler import LifeControler
from app.controller.explosion_controller import ExplosionControler
from app.controller.score_controller import ScoreController
from app.interfaces.start_screen import start_interface
from app.interfaces.game_over_screen import game_over_interface

# pylint: disable=no-member

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(setting.WINDOWS)
pygame.display.set_caption(setting.TITLE)
clock = pygame.time.Clock()
# Load the image for the icon
icon_image = pygame.image.load(setting.JECT1)
# Set the icon for the window
pygame.display.set_icon(icon_image)
# Set background images for window
background = pygame.image.load(setting.BACKGROUND).convert()
background = pygame.transform.scale(background, setting.WINDOWS)

# Cargar sonidos
laser_sound = pygame.mixer.Sound(setting.LASER_SOUND)
explosion_sound = pygame.mixer.Sound(setting.EXPLOSION_SOUND)
pygame.mixer.music.load(setting.MAIN_THEME)
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops=-1)

# Game Loop initializer
game_start: bool = True
game_over: bool = False
running: bool = True

# Game Loop
while running:
    if game_start:
        start_interface(screen, clock)
        game_start: bool = False
        all_sprites = pygame.sprite.Group()
        meteor_list = pygame.sprite.Group()
        bullets = pygame.sprite.Group()

        player = PlayerControler()
        all_sprites.add(player)

        for i in range(8):
            meteor = MeteorController()
            all_sprites.add(meteor)
            meteor_list.add(meteor)

        # Marcador / Score
        score: int = 0
    # Keep loop running at the right speed
    if game_over:
        game_over_interface(screen, clock)
        game_over: bool = False
        all_sprites = pygame.sprite.Group()
        meteor_list = pygame.sprite.Group()
        bullets = pygame.sprite.Group()

        player = PlayerControler()
        all_sprites.add(player)

        for i in range(8):
            meteor = MeteorController()
            all_sprites.add(meteor)
            meteor_list.add(meteor)

        # Marcador / Score
        score: int = 0

    clock.tick(60)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running: bool = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot(all_sprites, bullets)

    # Update
    all_sprites.update()

    # Colisiones meteoro - laser
    hits = pygame.sprite.groupcollide(meteor_list, bullets, True, True)
    for hit in hits:
        score += 1
        explosion_sound.play()
        explosion = ExplosionControler(hit.rect.center)
        all_sprites.add(explosion)

        meteor = MeteorController()
        all_sprites.add(meteor)
        meteor_list.add(meteor)

    # Colisiones jugador - meteoro
    hits = pygame.sprite.spritecollide(
        player, meteor_list, True)  # Change here
    for hit in hits:
        player.shield -= 25
        meteor = MeteorController()
        all_sprites.add(meteor)
        meteor_list.add(meteor)
        if player.shield <= 0:
            # running = False

            game_over: bool = True

    # Draw / Render
    screen.blit(background, [0, 0])
    all_sprites.draw(screen)

    # Marcador
    marker = ScoreController((8, 10), 16)
    marker.update(str(score))
    marker.draw(screen)

    # ESCUDO.
    life_bar = LifeControler((setting.WINDOWS_WIDTH - 180, 20))
    # life_bar.drawing(screen,  player.shield)
    life_bar.draw_on_frame(screen,  player.shield)
    pygame.display.flip()

pygame.quit()


