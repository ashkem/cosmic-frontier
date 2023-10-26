"""Module to load interface background image."""
import pygame
from config import setting

def load_interfase_background(path):
    """
    Load the interface background image with specified settings.

    Args:
        path (str): The path to the background image file.

    Returns:
        pygame.Surface: The loaded and scaled interface background image.
    """
    image = pygame.image.load(path).convert()
    image = pygame.transform.scale(image, setting.WINDOWS)
    return image
