"""Module for drawing text."""
import pygame
from config import setting


def draw_text(surface, text, size, x, y):
    """
    Draw text on a surface at a specified position.

    Args:
        surface (pygame.Surface): The surface on which the text will be drawn.
        text (str): The text to be drawn.
        size (int): The font size of the text.
        x (int): The x-coordinate of the position where the text will be drawn.
        y (int): The y-coordinate of the position where the text will be drawn.
    """
    font = pygame.font.SysFont(
        "serif", size)  # Load a font from the system fonts
    # Render the text with antialiasing and white color
    text_surface = font.render(text, True, setting.WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)  # Set the position of the text
    # Draw the text on the surface at the specified position
    surface.blit(text_surface, text_rect)
