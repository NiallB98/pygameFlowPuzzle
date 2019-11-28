import numpy as np
import pygame as pg

DGREY = (15, 15, 15)
colourEmpty = DGREY

def checkDone(hitboxes):
    done = True
    for hitbox in hitboxes:
        if (hitbox.isSrc == False) and ((hitbox.connection[0] == None) or (hitbox.connection[2] == None)):
            done = False
            break
    
    return done

def updateAge(sq, newAge, nextSq=None, grid=None):
    sq.age = newAge
    newAge += 1
    
    if nextSq != None:
        if ((nextSq.connection[0] != sq.i) or (nextSq.connection[1] != sq.j)) and (nextSq.isSrc == False) and (nextSq.connection[0] != None):
            nextConnection = grid[nextSq.connection[0], nextSq.connection[1]]
        elif (nextSq.isSrc == False) and (nextSq.connection[2] != None):
            nextConnection = grid[nextSq.connection[2], nextSq.connection[3]]
        else: nextConnection = None
        
        if nextConnection != None: updateAge(nextSq, newAge, nextConnection, grid)
    if nextSq.isSrc == True:
        nextSq.age = newAge

def crawlToSrc(sq, grid):
    
    if sq.connection[0] != None:
        connectedSq1 = grid[sq.connection[0], sq.connection[1]]
    else:
        connectedSq1 = None
    if sq.connection[2] != None:
        connectedSq2 = grid[sq.connection[2], sq.connection[3]]
    else:
        connectedSq2 = None
    
    # Compares connected squares' age values and keeps the oldest and removes line from the other and its connections, and updates age value of remaining line
    if (connectedSq1 != None) and (connectedSq2 != None):
        if connectedSq1.age > connectedSq2.age:
            connection(sq, connectedSq2, True)
            jumpBackToTarget(connectedSq2, sq, grid)
            goodConnection = connectedSq1
        else:
            connection(sq, connectedSq1, True)
            jumpBackToTarget(connectedSq1, sq, grid)
            goodConnection = connectedSq2
            
    elif (connectedSq1 == None) and (connectedSq2 != None):
        goodConnection = connectedSq2
        
    elif (connectedSq1 != None) and (connectedSq2 == None):
        goodConnection = connectedSq1
        
    updateAge(sq, 1, goodConnection, grid)

def jumpBackToTarget(sq, target, grid):
    
    # Clearing Connections For Square
    if (sq.connection[0] != None) and (sq.connection[1] != None) and (sq != target) and (sq.isSrc == False):
        nextSq = grid[sq.connection[0], sq.connection[1]]
        
        connection(sq, nextSq, True)
        changeState(sq, colourEmpty)
        
        # Recursion
        jumpBackToTarget(nextSq, target, grid)
    if (sq.connection[2] != None) and (sq.connection[3] != None) and (sq != target) and (sq.isSrc == False):
        nextSq = grid[sq.connection[2], sq.connection[3]]
        
        connection(sq, nextSq, True)
        changeState(sq, colourEmpty)
        
        # Recursion
        jumpBackToTarget(nextSq, target, grid)
    # Lone non-source square with no more connections
    if (sq.connection == [None, None, None, None]) and (sq != target) and (sq.isSrc == False):
        changeState(sq, colourEmpty)
    # Other Source
    if (sq != target) and (sq.isSrc == True):
        connection(sq, removeall=True)
    

def connection(sq, connect=None, remove=False, removeall=False, stopAfter=False):
    
    # Adding Connection Both Ways
    if (sq.connection[0] == None) and (sq.connection[1] == None) and (remove == False) and (connect != None):
        sq.connection[0] = connect.i
        sq.connection[1] = connect.j
        
        if (connect.connection[0] == None) and (connect.connection[1] == None):
            connect.connection[0] = sq.i
            connect.connection[1] = sq.j
        else:
            connect.connection[2] = sq.i
            connect.connection[3] = sq.j
            
        # Updating Connected Boolean
        if sq.connected == False: sq.connected = True
        if connect.connected == False: connect.connected = True
    elif (sq.connection[2] == None) and (sq.connection[3] == None) and (remove == False) and (connect != None):
        sq.connection[2] = connect.i
        sq.connection[3] = connect.j
        
        if (connect.connection[0] == None) and (connect.connection[1] == None):
            connect.connection[0] = sq.i
            connect.connection[1] = sq.j
        else:
            connect.connection[2] = sq.i
            connect.connection[3] = sq.j
        
        # Updating Connected Boolean
        if sq.connected == False: sq.connected = True
        if connect.connected == False: connect.connected = True
    # Removing Connection Both Ways
    elif (removeall == False) and (connect != None):
        if (sq.connection[0] == connect.i) and (sq.connection[1] == connect.j):
            sq.connection[0] = sq.connection[1] = None
            
            if (connect.connection[0] == sq.i) and (connect.connection[1] == sq.j):
                connect.connection[0] = connect.connection[1] = None
            else:
                connect.connection[2] = connect.connection[3] = None
            
            # Updating Connected Boolean
            if sq.connection == [None, None, None, None]:
                sq.connected = False
            elif sq.connected == False:
                sq.connected = True
                
            if connect.connection == [None, None, None, None]:
                connect.connected = False
            elif connect.connected == False:
                connect.connected = True
        else:
            sq.connection[2] = sq.connection[3] = None
            
            if (connect.connection[0] == sq.i) and (connect.connection[1] == sq.j):
                connect.connection[0] = connect.connection[1] = None
            else:
                connect.connection[2] = connect.connection[3] = None
            
            # Updating Connected Boolean
            if sq.connection == [None, None, None, None]:
                sq.connected = False
            elif sq.connected == False:
                sq.connected = True
                
            if connect.connection == [None, None, None, None]:
                connect.connected = False
            elif connect.connected == False:
                connect.connected = True
    # Remove All Connections
    else:
        sq.connection = [None, None, None, None]
        # Updating Connected Boolean
        sq.connected = False

def changeState(sq1, clr, lineColour=None, isSrc=False, sq2=None, num=None):
    sq1.colour = clr
    if lineColour != None:
        sq1.lineColour = lineColour
        
    else:
        sq1.lineColour = clr
        sq1.age = 0
    sq1.isSrc = isSrc
    
    if sq1.isSrc == True: sq1.lineComplete = False
    
    if sq2 != None:
        sq2.colour = clr
        if lineColour != None:
            sq2.lineColour = lineColour
        else:
            sq2.lineColour = clr
        sq2.isSrc = isSrc
        if sq2.isSrc == True: sq2.lineComplete = False
    
    if num != None:
        sq1.num = num
        if sq2 != None: sq2.num = num

def drawLines(hitboxes, win, grid, dx):
    for hitbox in hitboxes:
        if hitbox.connected == False:
            continue
        
        if (hitbox.connection[0] != None) and (hitbox.connection[1] != None):
            connectedBox = grid[hitbox.connection[0], hitbox.connection[1]]
            pg.draw.line(win, hitbox.lineColour, (hitbox.x + (0.5 * dx), hitbox.y + (0.5 * dx)), (connectedBox.x + (0.5 * dx), connectedBox.y + (0.5 * dx)), int(np.floor(dx / 5)))
            pg.draw.circle(win, hitbox.lineColour, (int(round(hitbox.x + (0.5 * dx))), int(round(hitbox.y + (0.5 * dx)))), int(np.floor(dx / 10)))
            
        if (hitbox.connection[2] != None) and (hitbox.connection[3] != None):
            connectedBox = grid[hitbox.connection[2], hitbox.connection[3]]
            pg.draw.line(win, hitbox.lineColour, (hitbox.x + (0.5 * dx), hitbox.y + (0.5 * dx)), (connectedBox.x + (0.5 * dx), connectedBox.y + (0.5 * dx)), int(np.floor(dx / 5)))
            pg.draw.circle(win, hitbox.lineColour, (int(round(hitbox.x + (0.5 * dx))), int(round(hitbox.y + (0.5 * dx)))), int(np.floor(dx / 10)))

def drawGrid(win, grid, lineColour, n, x0, x1, dx, dragging, colourEmpty, selectedColour):
    for i in range(0, n + 1):
        if i != n:
            for j in range(0, n):
                if (dragging and (grid[i, j].colour == selectedColour)) or grid[i, j].connected == False:
                    grid[i, j].drawSq(win, dx, colourEmpty)
                else:
                    grid[i, j].drawSq(win, dx)
                if grid[i, j].isSrc: grid[i, j].drawCirc(win, dx)
    # So the Lines are on top
    for i in range(0, n + 1):
        if i != n:
            X0 = x0 + (dx * i)
            Y0 = x0 + (dx * i)
            X1 = x0 + (dx * i)
            Y1 = x0 + (dx * i)
        else:
            X0 = x0 + (dx * i) - 1
            Y0 = x0 + (dx * i) - 1
            X1 = x0 + (dx * i) - 1
            Y1 = x0 + (dx * i) - 1
        # Vertical Lines
        pg.draw.line(win, lineColour, (X0, x0), (X1, x1), 3)
        # Horizontal Lines
        pg.draw.line(win, lineColour, (x0, Y0), (x1, Y1), 3)