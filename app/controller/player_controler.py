"""
This script defines a PlayerControler class that manages the behavior of the player. 
The class handles the initialization of the player's attributes such as position, speed, and image.
It provides methods for updating the player's position based on input from the user,
as well as a method for shooting bullets.

"""
import pygame
from config import setting
from app.controller.bullet_controller import BulletControler

# pylint: disable=no-member

class PlayerControler(pygame.sprite.Sprite):
    """;anages the behavior of the player in a game implemented using the Pygame module.

    Attributes:
        image (Surface): The image representing the player.
        rect (Rect): The rectangular area occupied by the player on the screen.
        speed_x (int): The horizontal speed at which the player moves.
        shield (int): The player's shield level.

    Methods:
       __init__(self): Initializes the controler with for position and shield level.
       update(self): Updates the player's position based on user input.
       shoot(self, all_sprites, bullets): Creates a new bullet from the player's 
       position and adds it to the list of all sprites and the group of bullets.
    """

    def __init__(self):
        """Initialize the PlayerControler with default attributes for position and shield level."""
        super().__init__()
        self.image = pygame.image.load(setting.JECT1).convert()
        self.image.set_colorkey(setting.BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = setting.WINDOWS_WIDTH // 2
        self.rect.bottom = setting.WINDOWS_HEIGHT - 10
        self.speed_x = 0

        self.shield = 100

    def update(self):
        """
        Update the player's position based on user input.
        Ensure that the player stays within the screen boundaries.
        """
        self.speed_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -5
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 5
        self.rect.x += self.speed_x
        if self.rect.right > setting.WINDOWS_WIDTH:
            self.rect.right = setting.WINDOWS_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self, all_sprites, bullets):
        """
        Create a new bullet from the player's position and add it to 
        the list of all sprites and the group of bullets.

        Args:
            all_sprites (Group): The group of all sprites in the game.
            bullets (Group): The group of bullets in the game.
        """
        bullet = BulletControler(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
