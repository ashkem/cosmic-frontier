"""
This script defines a controller class that manages the behavior of meteors in a game implemented.
The class handles the initialization of meteor attributes such as position, speed, and appearance.
It provides a method for updating the meteor's position based on its speed and repositioning 
it when it moves beyond the screen boundaries.
"""

import random
import pygame
from config import setting


class MeteorController(pygame.sprite.Sprite):
    """A class that manages the behavior of meteors in a game implemented using the Pygame module.

    Attributes:
        meteor_images (List): A list of meteor images used in the game.
        image (Surface): The current image representing the meteor.
        rect (Rect): The rectangular area occupied by the meteor on the screen.
        speedy (int): The vertical speed at which the meteor moves.
        speedx (int): The horizontal speed at which the meteor moves.

    Methods:
        __init__(self): Initializes the controller with random attributes for position and speed.
        update(self): Updates the meteor's position based on its speed.
    """

    def __init__(self):
        """Initialize the MeteorController with random attributes for position and speed."""
        super().__init__()
        self.meteor_images = [pygame.image.load(
            img).convert() for img in setting.METEORS_LIST]
        self.image = random.choice(self.meteor_images)
        self.image.set_colorkey(setting.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(setting.WINDOWS_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 10)
        self.speedx = random.randrange(-5, 5)

    def update(self):
        """
        Update the meteor's position based on its speed. 
        If the meteor moves beyond the screen boundaries, it is repositioned randomly.
        """
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > setting.WINDOWS_HEIGHT + 10 or self.rect.left < -25 or\
                self.rect.right > setting.WINDOWS_WIDTH + 22:
            self.rect.x = random.randrange(
                setting.WINDOWS_WIDTH - self.rect.width)

            # Change this variable
            self.rect.y = random.randrange(-150, -100)
            self.speedy = random.randrange(1, 8)
