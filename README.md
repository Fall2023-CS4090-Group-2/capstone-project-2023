# Mining Answers with Joe

![image](https://github.com/Fall2023-CS4090-Group-2/capstone-project-2023/assets/103133688/fc69d891-8457-424c-a51f-83cd0dfef740)

<!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->
<br/><center></center>
<!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->

## ⛏️: Introduction

We developed Mining Answers with Joe as a way for people to not only study content, but have fun doing so.  
Our project seeks to add a fun and exciting game component to an otherwise ordinary and boring way of studying.  
Mining Answers with Joe is meant to be universal, meaning that all players are able to customize their gaming experience, topic of study, difficulty, and more!     

<!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->
<br/><center></center>
<!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->

## ⛏️: Getting Started

**To begin your journey with Joe Miner, start a new game ...**  

1. Select your `difficulty` on the main menu screen  
    
2. Next, click `Play` and have fun while you study!  

<!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->
<br/><center></center>
<!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->

## ⛏️: How to Play

### Objective <a id="objective"/> 

Your goal is to obtain the highest possible score before you lose all of your health.     
Boulders will move towards you at a speed determined by the difficulty you chose on the main menu screen.    
Answer the question on the right of the screen to receive pickaxes.   
Move Joe Miner around to avoid the boulders or destroy them with your pickaxes to increase your score.    
Your `Health` , `Score` , and `Pickaxes` are displayed at the top left of your screen.  


![image](https://github.com/Fall2023-CS4090-Group-2/capstone-project-2023/assets/103133688/b7b8b692-d6b8-4276-919b-dc94568cc7b1)


### Movement <a id="movement"/>   

Use either the `arrow` keys or the `WASD` keys to move Joe Miner around.  

### Answering Questions <a id="answeringquestions"/>     

| Type              | Text-box?             | How-to    |
| :---------------- | :-------------------- | :-------- |
| Free Response     | Yes                   | Press `enter` and you will see the `Answer` box at the bottom of the screen turn green which indicates that you are now in Answer Mode and can begin typing your answer to the question. When you are finished with your answer, press `enter` again to submit your answer. | 
| Multiple Choice   | No                    | Select the correct answer using keys `1 2 3 4` |

_\*Note: After answering you will be in Normal Mode and will need to press `enter` again to switch to Answer Mode._    

| Normal Mode                  | Answer Mode                                  |
| :--------------------------: | :------------------------------------------: |
|![image](https://github.com/Fall2023-CS4090-Group-2/capstone-project-2023/assets/103133688/daa32fa9-b86b-4aaf-a16f-d689badf681b)|![image](https://github.com/Fall2023-CS4090-Group-2/capstone-project-2023/assets/103133688/8e0f9809-0909-402e-8718-ef557fe88de0)|

### Throwing <a id="throwing"/>    

Joe Miner's main weapon is his pickaxe. Throw his pickaxe at the approaching boulders using the `space` bar.  

### Pause <a id="pause"/>    

Press the `esc` key at any time to pause the game and weigh your options ...  

<!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->
<br/><center></center>
<!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->

## ⛏️: Additional Controls

### Toggle Music <a id="togglemusic"/>     

Click the `Toggle Music` button to turn music on/off    

### Skip Question <a id="skipquestion"/>   

Press the `r` key to skip to the next question

<!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->
<br/><center></center>
<!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->

## ⛏️: Project Structure

`main.py` - Entrypoint into game. Can change screen resolution here

`game.py` - Contains most of game logic when involving entities interacting

`entity.py` - Every object that appears on the screen has parent class of Entity. The class is just positional values and the picture for object.

`player.py` - The object that the user will control. Contains functions to move the player.

`enemy.py` - Object that will do damage to player. Has unique movement function.

`bullet.py` - Object the player fires. In our current implementation the bullet can only be fired if the user answers a question correctly.

`question.py` - Basic data structure for quesitons

<!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->
<br/><center></center>
<!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->

## ⛏️: TODO

Current tasks and issues can be found [here](https://github.com/orgs/Fall2023-CS4090-Group-2/projects/1/views/1)

<!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->
<br/><center></center>
<!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->

# ⛏️: Thanks for playing!
