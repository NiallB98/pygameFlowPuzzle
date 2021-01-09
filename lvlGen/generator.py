import os
import numpy as np

def numColourBeside(i, j, grid, colour=-1): # Returns Number of Squares That Are Empty Around Current
    count = 0
    if grid[i, j - 1] == colour: count += 1 # ABOVE
    if grid[i, j + 1] == colour: count += 1 # BELOW
    if grid[i - 1, j] == colour: count += 1 # LEFT
    if grid[i + 1, j] == colour: count += 1 # RIGHT
    return count

def notClosedOff(i, j, grid):
    
    if numColourBeside(i, j, grid) > 1: return True
    elif numColourBeside(i, j, grid) == 1:
        pass
    else: return False

#######

n = 8 # PLACEHOLDER

### [Stage 1: Creating Grid From Specified Dimension] ### (Done)

grid = np.zeros(shape=(n + 2, n + 2)) - 1
for i in range(n + 2):
    for j in range(n + 2):
        if (i == 0) or (j == 0) or (i == n + 1) or (j == n + 1):
            grid[i, j] = -2
            
level = grid # This grid will only store the source points
            
print(f'|GRID MADE|\n{grid}\n')

### [Stage 2: Creating Pre-solved Puzzle] ### (Unfinished)

numSq = n**2
numColours = min(15, n) - np.random.randint(0, 2) # (Min so that at max numColours is 15, allowing for the final 16th colour to be added if needed)
nLeft = numColours

print(f'numColours = {numColours}\n')

#while numSq > 0:
#    ###(assigning line length randomly based on what length is left)###
#    if numSq - (nLeft - 1) * 3 != 3: lineLength = random.randint(3, numSq - (nLeft - 1) * 3)
#    else: lineLength = 3
#    
#    ###(placing start point randomly in a place that fits)###
#    if 
#    
#    ###(snaking along grid till length has run out)###
#    
#    
#    ###(Updating numSq and number of lines left)###
#    numSq -= lineLength
#    nLeft -= 1

### [Stage 3: Stripping Off Boundaries of Level] ### (Done)

level = level[:,:n+1]
level = level[:n+1,:]
level = level[:,1:]
level = level[1:,:]

print(f'|FINAL LEVEL|\n{level}\n')

### [Stage 4: Returning Level] ### (Done)

#return grid, numColours, n

###


# =============================================================================
# Placeholder Level Generator (Same level every time)
# =============================================================================

def genLevel(n):
    
    if n == 5:
        lines = np.array([
        [-1, 0, 1, 2, -1],
        [-1, -1, -1, 3, -1],
        [-1, -1, 3, -1, -1],
        [0, -1, -1, 4, -1],
        [1, -1, 4, 2, -1]
        ])
    elif n == 6:
        lines = np.array([
        [0, 1, -1, 2, 3, 4],
        [-1, 0, -1, -1, -1, -1],
        [5, 1, -1, 2, -1, -1],
        [-1, -1, -1, 5, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [3, 4, -1, -1, -1, -1]
        ])
    elif n == 7:
        lines = np.array([
        [-1, -1, -1, -1, 0, -1, -1],
        [-1, 1, 2, -1, -1, -1, -1],
        [-1, -1, -1, -1, 2, -1, -1],
        [3, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, 4, 1, -1, -1],
        [-1, 3, -1, -1, -1, -1, -1],
        [-1, -1, -1, 4, 0, -1, -1]
        ])
    elif n == 8:
        lines = np.array([
        [-1, -1, -1, -1, -1, -1, 0, 1],
        [-1, -1, -1, 2, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 2, -1, 3, -1, -1, 4, -1],
        [-1, 0, -1, -1, -1, 1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 3, -1, -1, -1, -1, -1, -1],
        [-1, 4, 5, -1, -1, -1, -1, 5]
        ])
    elif n == 9:
        lines = np.array([
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 0, 1, 2, -1, -1, -1, -1, -1],
        [-1, -1, -1, 1, 3, -1, 3, 2, -1],
        [-1, -1, -1, -1, -1, -1, -1, 4, -1],
        [-1, 5, -1, 5, 0, -1, -1, -1, -1],
        [6, 4, -1, -1, -1, -1, -1, 7, 8],
        [-1, 8, 6, -1, -1, -1, -1, -1, -1],
        [-1, 7, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1]
        ])
    else:
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
    numColours = np.amax(level) + 1
    
    return lines, numColours
