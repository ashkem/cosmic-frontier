"""
Main Display script for running the game.
This script initializes the handles the display of the game's start interface.
"""
import pygame
from app.utils.create_button import Buttons
from app.utils.load_stage_bg import load_interfase_background
from app.utils.display_images import ImageDisplay
from config import setting

# pylint: disable=no-member

def start_interface(screen, clock):
    """
    Display the start interface with buttons.

    Args:
        screen (pygame.Surface): The screen surface to display the interface on.
        clock (pygame.time.Clock): The Pygame clock to regulate the frame rate.

    Displays the start interface with a background, a logo, and two buttons.
    Allows the user to interact with the interface by clicking on the buttons to start the game or exit the application.
    """
    screen.blit(load_interfase_background(setting.MAIN_BACKGROUND), [0, 0])
    logo = ImageDisplay(setting.STAR_LOGO, (500, 500))
    logo.display(screen, 10)
    button_star = Buttons(setting.START_BUTTON, (300, 450))

    button_star.draw(screen)

    button_exit = Buttons(setting.EXIT_BUTTON, (500, 450))

    button_exit.draw(screen)

    pygame.display.flip()
    waiting: bool = True
    while waiting:
        clock.tick(60)
        for start_event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            if start_event.type == pygame.QUIT:
                pygame.quit()
            if start_event.type == pygame.MOUSEBUTTONDOWN:
                if button_exit.button_rect.collidepoint(mouse_pos):
                    pygame.quit()
                if button_star.button_rect.collidepoint(mouse_pos):
                    waiting: bool = False
