import numpy as np

"""
[PLANNING]


    Rules:
        
    - Weigh where to start new line
    - Dont let line extend again in the same direction unless it cant go in any other direction
    - If a line has more length to use but cant extend any more give more length to a new line
    - Every line but last cannot create a 1-2 block empty space
    - Randomly set lengths of lines then the last one is given a number to fill the rest
    - When creating a line, ask it how many blocks it extends across
    - Give lines a random max length to extend for a certain number of steps
    - The new addition to the line cannot have >1 blocks of the same colour next to it
    - Empty boxes keep track of the number of empty boxes beside them
    - If adjEmpty == 1 then place the start of a new line
    - After all possible lines have been made and there is still empty space the program redoes lines
    - Any 2x2 grid from inside the overall grid cannot be the same colour

[PSEUDO CODE]

numColours = %
n = 9
grid = numpy.zeros(shape=(n + 2, n + 2)) - 1
for i in range(n + 2):
    for j in range(n + 2):
        if (i == ) or (j == -0) or (i == n + 1) or (j == n + 1):
            grid[i, j] = -2
            
print(grid)

numSq = gridSize^2

nLeft = numColours

while numSq > 0:
    ###(assigning line length randomly based on what length is left)###
    if numSq - (nLeft - 1) * 3 != 3: lineLength = random.randint(3, numSq - (nLeft - 1) * 3)
    else: lineLength = 3
    
    ###(placing start point randomly in a place that fits)###
    if 
    
    ###(snaking along grid till length has run out)###
    
    
    ###(Updating numSq and number of lines left)###
    numSq -= lineLength
    nLeft--

"""
#######

def numPossibleMoves(i, j, grid): # Returns Number of Squares That Are Empty Around Current
    count = 0
    if grid[i, j - 1] == -1: count += 1 # ABOVE
    if grid[i, j + 1] == -1: count += 1 # BELOW
    if grid[i - 1, j] == -1: count += 1 # LEFT
    if grid[i + 1, j] == -1: count += 1 # RIGHT
    return count

def notClosedOff(i, j, grid):
    
    if numPossibleMoves(i, j, grid) > 1: return True
    elif numPossibleMoves(i, j, grid) == 1:
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