"""Module for representing buttons in Pygame."""
import pygame


class Buttons:
    """
    Initializes a button object with images and initial settings.

    Args:
        normal_path (str): The path of the normal state button image file.
        hover_path (str): The path of the button image file in the hover state.
        coordinates (tuple): The coordinates (x, y) to position the button on the screen.
    """

    def __init__(self, normal_path: str, coordinates: tuple[int, int]):
        self.scale: tuple[int, int] = (150, 50)
        self.button_normal = pygame.image.load(normal_path)
        self.button_normal = pygame.transform.scale(
            self.button_normal, self.scale)
        self.button_rect = self.button_normal.get_rect()
        self.button_rect.center = coordinates

    def draw(self, screen):
        """
        Draws the button on the screen.

        Args:
            screen: The screen surface on which the button will be drawn.
        """
        screen.blit(self.button_normal, self.button_rect)
