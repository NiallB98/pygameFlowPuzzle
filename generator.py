import numpy as np

"""
[PLANNING]


    Rules:
        
    - Weigh where to start new line
    - Dont let line extend again in the same direction unless it cant go in any other direction
    - If a line has more length to use but cant extend any more give more length to a new line
    - Every line but last cannot create a ❤ block empty space
    - Randomly set lengths of lines then the last one is given a number to fill the rest
    - When creating a line, ask it how many blocks it extends across
    - Give lines a random max length to extend for a certain number of steps
    - The new addition to the line cannot have >1 blocks of the same colour next to it
    - Empty boxes keep track of the number of empty boxes beside them
    - If adjEmpty == 1 then place the start of a new line
    - After all possible lines have been made and there is still empty space the program redoes lines

[PSEUDO CODE]

number of colours = %
grid size = %
number of squares = grid size^2

# 

"""

def genLevel():
    
    lines = np.array([
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,0],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,1,2,3,4,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,5,6,-1,-1],
    [-1,-1,-1,-1,-1,-1,3,4,-1,-1,7,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,5,-1,-1,-1,8,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,7,9,-1,-1,-1,-1,-1,-1,-1,6,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,10,-1,10,11,-1,-1],
    [-1,2,-1,-1,-1,-1,-1,-1,-1,12,-1,-1,-1,-1],
    [-1,13,-1,-1,-1,13,-1,9,-1,-1,12,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,8,11,-1,-1,-1],
    [-1,-1,14,-1,-1,-1,-1,14,-1,-1,-1,-1,-1,-1],
    [1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    ])
    
    lines = np.transpose(lines)
    
    return lines, 15, 14