import numpy as np
import pygame as pg
from functions import drawGrid, changeState, connection, jumpBackToTarget, crawlToSrc, updateAge, checkDone, drawLines
from objects import squares
from colourSchemes import colourScheme
from Level_Generation.generator import genLevel
pg.init()

# Creating Window
winHeight = 640
winWidth = 640
win = pg.display.set_mode((winWidth, winHeight))
pg.display.set_caption("Flow Free")
mouseCircle = pg.Surface((winWidth, winHeight), pg.SRCALPHA, 32)

lineColour = (45, 45, 45)
colourEmpty = (15, 15, 15)
bgColour = (40, 40, 40)
clrs = colourScheme()

# Grid
x0 = 0
x1 = winHeight

# Level Dimensions (5 for 5x5 up to 10 for 10x10)
n = 9

level, numColours = genLevel(n)

dx = round(x1 - x0) / n
x1 = x0 + (dx * n)

x = np.linspace(x0, x0 + ((n - 1) * dx), n)
y = np.linspace(x0, x0 + ((n - 1) * dx), n)
x += 2
y += 2

grid = {}
hitboxes = []
for i, X in enumerate(x):
    for j, Y in enumerate(y):
        grid[i, j] = squares(X, Y, colourEmpty, colourEmpty, dx, i, j, win)
        grid[i, j].prevSq = -1
        hitboxes.append(grid[i, j])
        grid[i, j].connection = [None, None, None, None]
        grid[i, j].connected = False
        grid[i, j].isSrc = False
        grid[i, j].lineComplete = False
        grid[i, j].age = 0
        if level[i, j] != -1:
            changeState(grid[i, j], clrs.colour[level[i, j]], clrs.lineColour[level[i, j]], True, num=level[i, j])

lineDone = [numColours]
for i, _ in enumerate(lineDone): lineDone[i] = False

dragging = False
running = True
prevPoint = None
selectedColour = None
mousePrevPos = None

clock = pg.time.Clock()
FPS = 60 # Frames Per Second

while running:
    # Time Delay
    clock.tick(FPS)
    
    ### Events ###
    # Quit With Esc Button
    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE]: # Esc Button
        running = False
        continue
    # Quitting by closing window
    for event in pg.event.get():
        # Quit With Close Button
        if event.type == pg.QUIT:
            running = False
            continue
        
        # Mouse Click
        if event.type == pg.MOUSEBUTTONDOWN:
            # LMB
            if event.button == 1:
                lmx, lmy = pg.mouse.get_pos()
                for hitbox in hitboxes:
                    
                    # Checking square is coloured
                    if hitbox.rect.collidepoint(lmx, lmy) and ((hitbox.connected == True) or (hitbox.isSrc == True)):
                        dragging = True
                        selectedColour = hitbox.colour
                        selectedLColour = hitbox.lineColour
                        prevPoint = hitbox
                    
                    # Reseting line if clicking on source
                    if hitbox.rect.collidepoint(pg.mouse.get_pos()) and dragging and (hitbox.isSrc == True) and (hitbox.colour == selectedColour):
                        for box in hitboxes:
                            if (box.colour == selectedColour) and (box != hitbox):
                                if box.isSrc == False:
                                    changeState(box, colourEmpty)
                                connection(box, removeall=True)
                        prevPoint = hitbox
                        connection(hitbox, removeall=True)
                        hitbox.age = 1
                    
                    # Clicking on non-source similarly coloured square that has two connections already
                    if hitbox.rect.collidepoint(pg.mouse.get_pos()) and dragging and (hitbox.isSrc == False) and (hitbox.colour == selectedColour) and (hitbox.connection[0] != None) and (hitbox.connection[2] != None):
                        crawlToSrc(hitbox, grid)
        
        # Mouse Unclick
        if event.type == pg.MOUSEBUTTONUP:
            #LMB
            if event.button == 1:
                if dragging == True:
                    dragging = False
            
    ###
        
    ### Dragging ###
    for hitbox in hitboxes:
        if dragging and (prevPoint != hitbox) and hitbox.rect.collidepoint(pg.mouse.get_pos()):
            if (abs(prevPoint.i - hitbox.i) == 1) and (abs(prevPoint.j - hitbox.j) == 0) or (abs(prevPoint.i - hitbox.i) == 0) and (abs(prevPoint.j - hitbox.j) == 1):
                # Dragging Back From Last Source
                if (prevPoint.connected == True) and (hitbox.colour == selectedColour) and prevPoint.isSrc and (hitbox.connection[0] != None) and (hitbox.connection[2] != None):
                    
                    if prevPoint.connection[0] != None: connectedbox = grid[prevPoint.connection[0], prevPoint.connection[1]]
                    else: connectedbox = grid[prevPoint.connection[2], prevPoint.connection[3]]
                    connection(connectedbox, prevPoint, True)
                    prevPoint.connected = False
                    jumpBackToTarget(connectedbox, hitbox, grid)
                    prevPoint = hitbox
                
                # Dragging Back to First Selected Source
                elif hitbox.isSrc and hitbox.connected and hitbox.colour == selectedColour:
                    for box in hitboxes:
                            if (box.colour == selectedColour) and (box != hitbox):
                                if box.isSrc == False:
                                    changeState(box, colourEmpty)
                                connection(box, removeall=True)
                    prevPoint = hitbox
                    connection(hitbox, removeall=True)
                    hitbox.age = 1
                
                # Dragging over unconnected, non-source square
                elif (hitbox.isSrc == False) and (hitbox.colour != selectedColour) and (hitbox.connected == False):
                    
                    if prevPoint.isSrc:
                        if prevPoint.i == prevPoint.connection[0] and prevPoint.j == prevPoint.connection[1]:
                            prevPoint.connection[0] = prevPoint.connection[1] = None
                        if prevPoint.i == prevPoint.connection[2] and prevPoint.j == prevPoint.connection[3]:
                            prevPoint.connection[2] = prevPoint.connection[3] = None
                        if (prevPoint.connection[0] == None) and (prevPoint.connection[1] == None) and (prevPoint.connection[2] == None) and (prevPoint.connection[3] == None):
                            prevPoint.connected = False
                    
                    if ((prevPoint.isSrc == True) and (prevPoint.connected == False)) or (prevPoint.isSrc == False):
                        # Update Square
                        changeState(hitbox, selectedColour, selectedLColour)
                        connection(hitbox, prevPoint)
                        updateAge(hitbox, 1, prevPoint, grid)
                        prevPoint = hitbox
                            
                elif (hitbox.isSrc == False) and (hitbox.colour != selectedColour) and (hitbox.connected == True):
                    # Get the square(s) connected to the split up one and remove the connection to them
                    crawlToSrc(hitbox, grid)
                    if hitbox.connection[0] != None: connection(hitbox, grid[hitbox.connection[0], hitbox.connection[1]], True)
                    if hitbox.connection[2] != None: connection(hitbox, grid[hitbox.connection[2], hitbox.connection[3]], True)
                    
                    # Update Square
                    changeState(hitbox, selectedColour, selectedLColour)
                    hitbox.connected = True
                    connection(hitbox, prevPoint)
                    updateAge(hitbox, 1, prevPoint, grid)
                    prevPoint = hitbox
                        
                # Dragging over the last source
                elif (hitbox.isSrc == True) and (hitbox.connected == False) and (hitbox.colour == selectedColour):
                    # Making sure square is beside previously selected square and not the same colour already
                    connection(hitbox, prevPoint)
                    updateAge(hitbox, 1, prevPoint, grid)
                    prevPoint = hitbox
                    
                    if checkDone(hitboxes):
                        print('Done')
                # Dragging over non-source similarly coloured non-source square
                elif (hitbox.connected == True) and (hitbox.colour == selectedColour) and (hitbox.isSrc == False):
                    jumpBackToTarget(prevPoint, hitbox, grid)
                    prevPoint = hitbox
            elif (prevPoint.connected == True) and (hitbox.colour == selectedColour) and prevPoint.isSrc and (hitbox.connection[0] != None) and (hitbox.connection[2] != None):
                    
                if prevPoint.connection[0] != None: connectedbox = grid[prevPoint.connection[0], prevPoint.connection[1]]
                else: connectedbox = grid[prevPoint.connection[2], prevPoint.connection[3]]
                connection(connectedbox, prevPoint, True)
                prevPoint.connected = False
                jumpBackToTarget(connectedbox, hitbox, grid)
                prevPoint = hitbox
            elif (hitbox.connected == True) and (hitbox.colour == selectedColour) and (hitbox.isSrc == False):
                jumpBackToTarget(prevPoint, hitbox, grid)
                prevPoint = hitbox
            # Hovering over start source from non-source after losing focus
            elif (hitbox.connected == True) and (hitbox.colour == selectedColour) and hitbox.isSrc and (prevPoint.isSrc == False):
                jumpBackToTarget(prevPoint, hitbox, grid)
                prevPoint = hitbox
            # Hovering over start source while prevPoint is the other source
            elif hitbox.connected and (hitbox.colour == selectedColour) and hitbox.isSrc and prevPoint.isSrc and (prevPoint.age < hitbox.age) and prevPoint.connected:
                if prevPoint.connection[0] != None: connectedbox = grid[prevPoint.connection[0], prevPoint.connection[1]]
                else: connectedbox = grid[prevPoint.connection[2], prevPoint.connection[3]]
                connection(connectedbox, prevPoint, True)
                prevPoint.connected = False
                jumpBackToTarget(connectedbox, hitbox, grid)
                prevPoint = hitbox
    
    ###
    
    # Filling Background
    background_image = pg.Surface(((winWidth, winHeight)))
    background_image.fill(bgColour)
    
    # Drawing Grid
    drawGrid(win, grid, lineColour, n, x0, x1, dx, dragging, colourEmpty, selectedColour)
    
    # Drawing Lines
    drawLines(hitboxes, win, grid, dx)
    
    # Drawing Mouse Circle
    if dragging:
        (rPart, gPart, bPart) = selectedLColour
        mouseColour = (rPart, gPart, bPart, 50)
        pg.draw.circle(mouseCircle, mouseColour, (int(pg.mouse.get_pos()[0]), int(pg.mouse.get_pos()[1])), 56)
    
    # Updating Display
    win.blit(mouseCircle, (0, 0))
    pg.display.update()
    
    mouseCircle.fill((255,255,255,0))
    mousePrevPos = pg.mouse.get_pos()
    
pg.quit()
