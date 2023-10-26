"""
This script defines a ScoreController that manages the game score display in a Pygame-based game.
The class handles the rendering of the score value on the screen and the graphical frame around it. 
It provides methods for updating the score value and drawing it onto the surface.

Attributes:
    value (int): The current score value.
    x (int): The x-coordinate for the score display's position.
    y (int): The y-coordinate for the score display's position.
    size (int): The font size for the score display.
    font (Font): The font object used for rendering the text.
    color (Tuple): The color of the text.
    frame_image (Surface): The frame image for the score display.

Methods:
    __init__(self, coord, size): Initializes the controller with coordinates and font size.
    update(self, value): Updates the score value to the provided value.
    draw(self, surface): Draws the score display along with the frame onto the specified surface.
"""

import pygame
from config import setting

# Load background.
class ScoreController:
    """A class that manages the game score display in a Pygame-based game.

    Attributes:
        value (int): The current score value.
        x (int): The x-coordinate for the score display's position.
        y (int): The y-coordinate for the score display's position.
        size (int): The font size for the score display.
        font (Font): The font object used for rendering the text.
        color (Tuple): The color of the text.
        frame_image (Surface): The frame image for the score display.

    Methods:
        __init__(self, coord, size): Initializes controller with the coordinates and font size.
        update(self, value): Updates the score value to the provided value.
        draw(self, surface): Draws the score with the frame onto the specified surface.
    """

    def __init__(self, coord, size):
        """Initialize the ScoreController with the specified coordinates and font size.

        Args:
            coord (Tuple): The (x, y) coordinates for the score display's position.
            size (int): The font size for the score display.
        """
        self.value = 0
        self.x = coord[0]
        self.y = coord[1]
        self.size = size
        self.font = pygame.font.SysFont("serif", size)
        self.color = setting.WHITE
        self.frame_image = pygame.image.load(setting.SCORE_FRAME)
        self.frame_image = pygame.transform.scale(self.frame_image, (150, 40))

    def update(self, value):
        """Update the score value to the provided value.

        Args:
            value (int): The new score value.
        """
        self.value = value

    def draw(self, surface):
        """Draw the score display along with the frame onto the specified surface.

        Args:
            surface (Surface): The surface on which to draw the score display.
        """
        text_surface = self.font.render(str(self.value), True, self.color)
        text_rect = text_surface.get_rect()
        # Adjusting the position of the text
        text_rect.midtop = (self.x + 75, self.y + 15)
        surface.blit(self.frame_image, (self.x, self.y))
        surface.blit(text_surface, text_rect)
