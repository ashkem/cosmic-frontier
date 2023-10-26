"""Module to load explosion images."""
import pygame
from config import setting

def explosion_load():
    """
    Load explosion images with specified settings.

    Returns:
        list: List of scaled explosion images.
    """
    image_path = []
    for img in setting.EXPLOSION_LIST:
        file = pygame.image.load(img).convert()
        file.set_colorkey(setting.BLACK)
        img_scale = pygame.transform.scale(file, (70, 70))
        image_path.append(img_scale)
    return image_path
