# Capstone 1 Project

## Project Structure

`main.py` - Entrypoint into game. Can change screen resolution here

`game.py` - Contains most of game logic when involving entities interacting

`entity.py` - Every object that appears on the screen has parent class of Entity. The class is just positional values and the picture for object.

`player.py` - The object that the user will control. Contains functions to move the player.

`enemy.py` - Object that will do damage to player. Has unique movement function.

`bullet.py` - Object the player fires. In our current implementation the bullet can only be fired if the user answers a question correctly.

`question.py` - Basic data structure for quesitons

# TODO

- [ ] Remove any entities that appear of screen
    - Bullets
    - Enemies?

- [ ] CLI arguments for game size and questions

- Bug with duplicate questions and removing when correct
