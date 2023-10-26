"""
Game over display script for running the game.
This script initializes the handles the display of the game over interface.
"""
import pygame
from app.utils.create_button import Buttons
from app.utils.load_stage_bg import load_interfase_background
from app.utils.display_images import ImageDisplay
from config import setting

# pylint: disable=no-member

def game_over_interface(screen, clock):
    """
    This function displays the game over interface, including the background, a game over text,
    and a replay button. It continuously checks for user input and exits the interface when the
    replay button is clicked.

    Args:
        screen (pygame.Surface): The main surface where elements are displayed.
        clock: The pygame clock object to manage the frame rate.

    Returns:
        None    
    """
    screen.blit(load_interfase_background(setting.GAME_OVER_BG), [0, 0])
    logo = ImageDisplay(setting.TXT_GAME_OVER, (250, 250))
    logo.display(screen)
    button_replay = Buttons(setting.REPLAY_BUTTON, (
        (setting.WINDOWS_WIDTH // 2),
        450
       )
     )
    button_replay.draw(screen)
    pygame.display.flip()
    waiting: bool = True
    while waiting:
        clock.tick(60)
        for game_event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            if game_event.type == pygame.QUIT:
                pygame.quit()
            if game_event.type == pygame.MOUSEBUTTONDOWN:
                #if button_replay.button_rect.collidepoint(mouse_pos):
                #    pygame.quit()
                if button_replay.button_rect.collidepoint(mouse_pos):
                    waiting: bool = False
