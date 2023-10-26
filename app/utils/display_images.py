"""Module to display an image centered on the screen."""

import pygame


class ImageDisplay:
    """
    Display an image on the screen.

    Args:
        image_path (str): The path to the image file.
        size (tuple): The dimension of the image file.
    """

    def __init__(self, image_path: str, size: tuple[int, int]):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, size)
        self.image_width, self.image_height = self.image.get_rect().size

    def get_large(self, screen_large, image_large):
        """get large"""
        return (screen_large // 2) - (image_large // 2)

    def display(self, screen, align_y=None):
        """
        Display the image on the screen.

        Args:
            screen (pygame.Surface): The surface on which the image will be displayed.
            horizontal (int, optional): The horizontal position of the image. Defaults to None.
        """
        screen_width, screen_height = screen.get_width(), screen.get_height()
        image_x = self.get_large(screen_width, self.image_width)
        center_y = self.get_large(screen_height, self.image_height)
        image_y = center_y if align_y is None else align_y

        screen.blit(self.image, (image_x, image_y))
