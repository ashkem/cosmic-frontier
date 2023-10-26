"""Class for controlling the health bar"""
import pygame
from config import setting


class LifeControler:
    """
       Initializes the LifeController class with the given coordinates.

       Args:
          coordinate (tuple): (x, y) coordinates of the health bar's position.    
    """

    def __init__(self, coordinate) -> None:
        self.life_length: int = 122  # Length of the health bar
        self.life_height = 10  # Height of the health bar
        self.x: int = coordinate[0]  # x position of the health bar
        self.y: int = coordinate[1]  # y position of the health bar
        self.frame_image = pygame.image.load(
            setting.LIFE_FRAME)  # Load the health bar frame image
        self.frame_image = pygame.transform.scale(
            self.frame_image, (150, 20))  # Adjust the size of the frame image

    def draw_on_frame(self, surface, percentage):
        """
        Draws the health bar on the frame of the image.

        Args:
            surface: Surface where the health bar will be drawn.
            percentage (int): Current health percentage.
        """
        frame_rect = self.frame_image.get_rect()
        # Set the position of the frame
        frame_rect.topleft = (self.x, self.y)
        # Draw the frame on the surface
        surface.blit(self.frame_image, frame_rect)

        # Calculate the x position for the health bar to be drawn in the center of the frame
        health_bar_x = self.x + (frame_rect.width - self.life_length) // 2
        health_bar_y = self.y + (frame_rect.height - self.life_height) // 2
        # Draw the health bar at the calculated position
        self.draw_health_bar(surface, percentage, health_bar_x, health_bar_y)

    def draw_health_bar(self, surface, percentage, health_bar_x, health_bar_y):
        """
        Draws the health bar on the specified surface at the specific position with rounded edges.

        Args:
            surface: Surface where the health bar will be drawn.
            percentage (int): Current health percentage.
            health_bar_x (int): x position of the health bar.
            health_bar_y (int): y position of the health bar.
        """
        fill_width = (percentage / 100) * self.life_length
        fill_rect = pygame.Rect(
            health_bar_x, health_bar_y, fill_width, self.life_height)
        border_rect = pygame.Rect(
            health_bar_x, health_bar_y, self.life_length, self.life_height)
        # Adjust the value of border_radius as needed
        pygame.draw.rect(surface, setting.GREEN,
                         fill_rect, border_radius=5)
