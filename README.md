# Space Invaders

## Introduction

We developed Space Invaders as a way for people to not only study content, but have fun doing so.  
Our project seeks to add a fun and exciting game component to an otherwise ordinary and boring way of studying.  
Space Invaders is meant to be universal, meaning that all players are able to customize their gaming experience,  
topic of study, difficulty, and many more!  

## Getting Started

**To begin your journey through space, create a new game ...**  
    1. Select your `difficulty` on the main menu screen  
    2. Next, click `Play` and enjoy while you study!  

## How to Play

**Objective**  

Your goal is to survive as long as possible while destroying the approaching enemies by answering questions before you lose all of your health.  

**Movement**  

Use either the arrow keys or the WASD keys to move Joe Miner around.  

**Answering Questions**  

To answer the questions, press `enter` and you will see the `Answer` text at the bottom of the screen turn yellow which indicates that you are now in Answer Mode   
and can begin typing your answer to any of the questions. When you are finished with your answer, press `enter` again to submit your answer.    

Note - after answering you will be in Normal Mode and will need to press `enter` again to switch to Answer Mode.   

**Shooting**  

Joe Miner's main weapon is his pickaxe. Fire his pickaxe at the approaching enemies using the `space` bar.  

**Pause**  

Press the `esc` key at any time to pause the game and weigh your options ...  

## Project Structure

`main.py` - Entrypoint into game. Can change screen resolution here

`game.py` - Contains most of game logic when involving entities interacting

`entity.py` - Every object that appears on the screen has parent class of Entity. The class is just positional values and the picture for object.

`player.py` - The object that the user will control. Contains functions to move the player.

`enemy.py` - Object that will do damage to player. Has unique movement function.

`bullet.py` - Object the player fires. In our current implementation the bullet can only be fired if the user answers a question correctly.

`question.py` - Basic data structure for quesitons

## TODO

Current tasks and issues can be found [here](https://github.com/orgs/Fall2023-CS4090-Group-2/projects/1/views/1)
