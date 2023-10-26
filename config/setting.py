"""
This file contains constants for the game.
It defines screen settings, colors, paths for images, and sounds.
"""

# DISPLAY SETTINGS
WINDOWS_WIDTH: int = 800  # Width of the game window.
WINDOWS_HEIGHT: int = 600  # Height of the game window.
WINDOWS: tuple[int, int] = (WINDOWS_WIDTH, WINDOWS_HEIGHT)

# FRAMES
# Path for the life frame image.
LIFE_FRAME: str = "./assets/img/buttons/tablero_vida.png"
SCORE_FRAME: str ="./assets/img/buttons/meteoritos.png"

#BUTTONS
START_BUTTON:str="assets/img/buttons/btn_start.png"
EXIT_BUTTON:str="assets/img/buttons/btn_exit.png"
REPLAY_BUTTON:str="assets/img/buttons/btn_replay.png"

# IMAGES PATHS
# Path for the background image.
BACKGROUND: str = "./assets/img/bg/background.png"
# Path for the main background image.
MAIN_BACKGROUND: str = "./assets/img/bg/pantalla_start.jpg"
# Path for the game over background image.
GAME_OVER_BG: str = "./assets/img/bg/pantalla_game_over.png"
# Path for the game over text image.
TXT_GAME_OVER: str = "./assets/img/text/game_over.png"
STAR_LOGO: str = "./assets/img/logo.png"
LASER: str = "./assets/img/laser/laser1.png"  # Path for the laser image.
JECT1: str = "./assets/img/characters/player.png"  # Path for the player image.

# List of paths for meteor images.
METEORS_LIST: list[str] = [
    "assets/img/meteoros/meteorGrey_big1.png",
    "assets/img/meteoros/meteorGrey_big2.png",
    "assets/img/meteoros/meteorGrey_big3.png",
    "assets/img/meteoros/meteorGrey_big4.png",
    "assets/img/meteoros/meteorGrey_med1.png",
    "assets/img/meteoros/meteorGrey_med2.png",
    "assets/img/meteoros/meteorGrey_small1.png",
    "assets/img/meteoros/meteorGrey_small2.png",
    "assets/img/meteoros/meteorGrey_tiny1.png"
]

# List of paths for explosion images.
EXPLOSION_LIST: list[str] = [
    "assets/img/explosion/regularExplosion00.png",
    "assets/img/explosion/regularExplosion01.png",
    "assets/img/explosion/regularExplosion02.png",
    "assets/img/explosion/regularExplosion03.png",
    "assets/img/explosion/regularExplosion04.png",
    "assets/img/explosion/regularExplosion05.png",
    "assets/img/explosion/regularExplosion06.png",
    "assets/img/explosion/regularExplosion07.png",
    "assets/img/explosion/regularExplosion08.png"
]

# SOUNDS PATHS
# Path for the explosion sound.
EXPLOSION_SOUND: str = "./assets/sounds/explosion.wav"
LASER_SOUND: str = "./assets/sounds/laser5.ogg"  # Path for the laser sound.
MAIN_THEME: str = "./assets/sounds/intro.ogg"  # Path for the main theme.

# COLORS
BLACK: tuple[int, int, int] = (0, 0, 0)  # Black color in RGB format.
YELLOW: tuple[int, int, int] = (255, 255, 204)  # White color in RGB format.
RED: tuple[int, int, int] = (255, 0, 0)  # Red color in RGB format.
WHITE: tuple[int, int, int] = (255, 255, 255)  # White color in RGB format.
GREEN: tuple[int, int, int] = (0, 255, 0)  # Green color in RGB format.
BLUE: tuple[int, int, int] = (0, 0, 255)  # Blue color in RGB format.
ORANGE: tuple[int, int, int] = (255, 69, 0)  # Orange color in RGB format.

# TEXT
TITLE: str = "Cosmic Frontier"  # Title text for the game.
# Instruction title text for the game.
INSTRUCTION_TITLE: str = "(Instructions)"
STAR_TITLE: str = "Press key to begin"  # Start title text for the game.
