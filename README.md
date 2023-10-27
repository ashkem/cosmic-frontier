# Cosmic Frontier

Este proyecto es un juego simple implementado en Python utilizando la biblioteca Pygame. Se trata de un juego espacial en el que el jugador controla una nave espacial y dispara para destruir meteoros, al mismo tiempo que evita colisiones y mantiene su nivel de escudo.

## Descripción

En Cosmic Frontier, el jugador asume el control de una nave espacial que debe sobrevivir a una lluvia de meteoros. El jugador puede disparar misiles para destruir los meteoros, pero debe tener cuidado de no colisionar con ellos. El jugador también debe mantener su nivel de escudo, ya que si se agota, el juego terminará.

## Instalación

1. Clona el repositorio:

   ```sh
   git clone https://github.com/tu_usuario/tu_proyecto.git
   ```

**CARACTERISTICAS:**

- **Interfaz de inicio atractiva:** El juego presenta una interfaz de inicio atractiva con un fondo visualmente agradable y botones para iniciar el juego o salir del mismo.

- **Mecánica de juego básica:** El juego parece ser un juego de disparos de desplazamiento lateral en el que el jugador controla un personaje que dispara a los meteoros que se desplazan desde la parte superior de la pantalla.

- **Elementos de sonido y música:** Se han incorporado efectos de sonido, como el sonido del láser y de la explosión, para mejorar la experiencia del juego. Además, se ha incluido música de fondo para aumentar la inmersión del jugador.

- **Sistema de puntuación:** El juego incluye un sistema de puntuación que aumenta cada vez que el jugador destruye un meteoro. Este sistema de puntuación podría estar relacionado con el progreso del jugador y su desempeño en el juego.

- **Gestión de la vida del jugador:** Se ha implementado un sistema de escudo para el jugador que disminuye cuando el jugador choca con un meteoro. Si el escudo alcanza cero, se activa una pantalla de juego terminado. Este sistema agrega un elemento de desafío al juego y requiere que los jugadores eviten los obstáculos para mantenerse en el juego.

## Ejecuta el juego

   ```sh
      python main.py
   ```

## Extructura de directorios

- /app
  - /controller
    - bullet_controller.py
    - explosion_controller.py
    - life_controller.py
    - meteor_controller.py
    - player_controller.py
    - score_controller.py
  - /interfaces
    - game_over_screen.py
    - start_screen.py
  - /utils
    - create_button.py
    - display_images.py
    - handle_draw_txt.py
    - handle_explosion.py
    - load_stage_bg.py
- /config
  - setting.py
- /assets
  - /img
  - /sounds
- main.py
- README.md
- LICENSE
- requirements.txt

## Agradecimientos

Agradezco a mi esposa **Roux Tabata** y todos los que han probar  **Cosmic Frontier**.

## Datos de contacto

Si tiene alguna pregunta o problema con Cosmic Frontier, no dude en ponerse en contacto conmigo:

   ```javaScript
      const contact ={
         Name:"Miguel Tabata",
         Nick:"Ashkem",
         Email:"miiguelangelotabata@gmail.com",
         SiteWeb:"https://erishyum.com"
      }
   ```
