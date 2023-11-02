# Cosmic Frontier

Este proyecto es un juego open sources implementado en Python utilizando la biblioteca Pygame. En Cosmic Frontier, el jugador controla una nave espacial, dispara para destruir meteoritos y evita colisiones para mantener su nivel de escudo.

## Descripción

Cosmic Frontier desafía a los jugadores a sobrevivir a una lluvia de meteoritos. La nave puede disparar misiles para destruir los meteoritos, pero colisionar con ellos disminuirá su nivel de escudo. Cuando el escudo se agota, el juego termina.

## Instalación

1. Clona el repositorio:

   ```sh
   git clone https://github.com/ashkem/cosmic-frontier.git
   ```

2. Ejecutar el juego

   ```sh
      python app.py
   ```

## Caracteristicas

- **Interfaz de inicio atractiva:** El juego presenta una interfaz de inicio atractiva con un fondo visualmente agradable y botones para iniciar el juego o salir del mismo.

- **Mecánica de juego básica:** El juego parece ser un juego de disparos de desplazamiento lateral en el que el jugador controla un personaje que dispara a los meteoritos que se desplazan desde la parte superior de la pantalla.

- **Elementos de sonido y música:** Se han incorporado efectos de sonido, como el sonido del láser y de la explosión, para mejorar la experiencia del juego. Además, se ha incluido música de fondo para aumentar la inmersión del jugador.

- **Sistema de puntuación:** El juego incluye un sistema de puntuación que aumenta cada vez que el jugador destruye un meteorito. Este sistema de puntuación podría estar relacionado con el progreso del jugador y su desempeño en el juego.

- **Gestión de la vida del jugador:** Se ha implementado un sistema de escudo para el jugador que disminuye cuando el jugador choca con un meteorito. Si el escudo alcanza cero, se activa una pantalla de juego terminado. Este sistema agrega un elemento de desafío al juego y requiere que los jugadores eviten los obstáculos para mantenerse en el juego.

## Controles

### Movimiento de la Nave

- Utiliza las teclas de dirección para mover la nave espacial:
  - ↑ (tecla de flecha arriba): Mover hacia arriba.
  - ↓ (tecla de flecha abajo): Mover hacia abajo.
  - ← (tecla de flecha izquierda): Mover hacia la izquierda.
  - → (tecla de flecha derecha): Mover hacia la derecha.

### Disparar

- Para disparar y destruir los meteoritos, utiliza la tecla de espacio (`␣`).

## Objetivo del Juego

Tu objetivo es sobrevivir el mayor tiempo posible en el espacio, destruyendo los meteoritos que se cruzan en tu camino. A medida que progresas, los meteoritos serán de diferentes tamaños y velocidades, lo que aumentará la dificultad del juego.

## Puntuación

Cada meteorito destruido suma puntos. ¡Intenta obtener la puntuación más alta y supera tus récords anteriores!

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

Agradezco a mi esposa **Roux Tabata**, que es el pilar de mi vida y ser el motor que me impulsa a superarme y enfrentar nuevos desafíos, gracias esposita linda por ser la fuente de inspiración para mi código y por último le agradezco a todos los que le brinden un pequeño tiempo en probar y compartir **Cosmic Frontier**, el cual es un juego hecho con amor.

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
