"""This script defines a BulletControler class that represents 
the bullets in a game implemented using the Pygame module. 
The bullets are used by the player to shoot and destroy meteors. 
The class initializes the bullet's position, speed, and appearance. 
The update method controls the movement of the bullet, 
and it is automatically removed from the game when it goes beyond the screen boundaries. 
The class utilizes Pygame's sprite functionality for easy integration into the game's main logic."""

import pygame
from config import setting


class BulletControler(pygame.sprite.Sprite):
    """A class that represents bullets in a game implemented using the Pygame module.

    Attributes:
        image (Surface): The visual representation of the bullet.
        rect (Rect): The rectangular area occupied by the bullet on the screen.
        speedy (int): The speed at which the bullet moves.

    Methods:
     __init__(self, x, y): Initializes the BulletControler with the specified x and y coordinates.
     update(self): Updates the position of the bullet, moving it upwards. 
        If the bullet moves beyond the screen boundaries, it is removed from the game.
    """

    def __init__(self, x, y):
        """Initialize the BulletControler with the specified x and y coordinates.

        Args:
            x (int): The x-coordinate for the bullet's initial position.
            y (int): The y-coordinate for the bullet's initial position.
        """
        super().__init__()
        self.image = pygame.image.load(setting.LASER)
        self.image.set_colorkey(setting.BLACK)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        """
         Update the position of the bullet, moving it upwards. 
         If the bullet moves beyond the screen boundaries, it is removed from the game.
        """
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
