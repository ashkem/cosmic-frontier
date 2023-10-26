"""
This script defines an ExplosionControler class that manages the explosion animation 
in a game implemented using the Pygame module. The class initializes the explosion's position, 
animation frames, and frame rate. It provides a method for updating the explosion animation 
and removing it from the game when the animation is complete.
"""
import pygame
from app.utils.handle_explosion import explosion_load


class ExplosionControler(pygame.sprite.Sprite):
    """A class that manages the explosion animation in a game implemented using the Pygame module.

    Attributes:
        explosion_anim (List): A list of images representing the frames of the explosion animation.
        image (Surface): The current image representing the explosion frame.
        rect (Rect): The rectangular area occupied by the explosion on the screen.
        frame (int): The current frame of the explosion animation.
        last_update (int): The time of the last update for the explosion animation.
        frame_rate (int): The time interval between each frame of the explosion animation.

    Methods:
        __init__(self, center): Initializes the controler with the coordinates for the explosion's.
        update(self): Updates the explosion animation by changing the displayed frame.
    """

    def __init__(self, center):
        """
        Initialize the controler with the specified center coordinates for the explosion's position.

        Args:
            center (Tuple): The (x, y) coordinates for the center of the explosion.
        """
        super().__init__()
        self.explosion_anim = explosion_load()
        self.image = self.explosion_anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50  # how long to wait for the next frame VELOCITY OF THE EXPLOSION

    def update(self):
        """
        Update the explosion animation by changing the displayed frame. 
        If the animation reaches the end, the explosion is removed from the game.
        """
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.explosion_anim):
                # if we get to the end of the animation we don't keep going.
                self.kill()
            else:
                center = self.rect.center
                self.image = self.explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
