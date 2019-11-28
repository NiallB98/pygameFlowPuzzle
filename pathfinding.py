import pygame as pg
# Pathfinding for when the mouse is moving too fast for the framerate to keep up

# Idea: Compare previous mouse position and current mouse position's i's and j's and the ratio of i/j to predict what way the user wants the line to go

def pathfind(dragging, hitbox, prevPoint, grid, colourEmpty, mousePrevPos, dx):
    if dragging and hitbox.rect.collidepoint(pg.mouse.get_pos()):
        # Checking that the hitbox is empty and not the prevPoint
        if hitbox != prevPoint and hitbox.colour == colourEmpty:
            
            ###### STRAIGHT LINE ######
            
            ### When Mouse is ABOVE in STRAIGHT line from prevPoint ###
            if (prevPoint.i == hitbox.i) and (hitbox.j < prevPoint.j):
                pass
            ### When Mouse is BELOW in STRAIGHT line from prevPoint ###
            elif (prevPoint.i == hitbox.i) and (hitbox.j > prevPoint.j):
                pass
            ### When Mouse is LEFT in STRAIGHT line from prevPoint ###
            elif (prevPoint.i > hitbox.i) and (hitbox.j == prevPoint.j):
                pass
            ### When Mouse is RIGHT in STRAIGHT line from prevPoint ###
            elif (prevPoint.i < hitbox.i) and (hitbox.j == prevPoint.j):
                pass
            
            ###### DIAGONAL ######
            # y = mx + c
            #
            # m = (mousey - prevy)/(mousex - prevx)
            # c = mousey - m * x
            # y >/< midpoint.y +/- dx
            #
            
            mx = pg.mouse.get_pos()[0]
            my = pg.mouse.get_pos()[1]
            prevmx = mousePrevPos[0]
            prevmy = mousePrevPos[1]
            grad = (my - prevmy) / (mx - prevmx)
            C = my - grad * mx
            
            if (prevPoint.i == hitbox.i + 1) and (prevPoint.j == hitbox.j - 1): # North-East
                midx = hitbox.x + dx
                midy = hitbox.y
                Y = midx  * grad + C
                
                if Y >= midy: # Right Then Up
                    pass
                else: # Up Then Right
                    pass
            if (prevPoint.i == hitbox.i + 1) and (prevPoint.j == hitbox.j + 1): # South-East
                midx = hitbox.x + dx
                midy = hitbox.y + dx
                Y = midx  * grad + C
                
                if Y <= midy: # Right Then Down
                    pass
                else: # Down Then Right
                    pass
            if (prevPoint.i == hitbox.i - 1) and (prevPoint.j == hitbox.j + 1): # South-West
                midx = hitbox.x
                midy = hitbox.y + dx
                Y = midx  * grad + C
                
                if Y <= midy: # Left Then Down
                    pass
                else: # Down Then Left
                    pass
            if (prevPoint.i == hitbox.i - 1) and (prevPoint.j == hitbox.j - 1): # North-West
                midx = hitbox.x
                midy = hitbox.y
                Y = midx  * grad + C
                
                if Y >= midy: # Left Then Up
                    pass
                else: # Up Then Left
                    pass
            
            ######