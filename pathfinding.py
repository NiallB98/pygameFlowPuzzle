import pygame as pg
# Pathfinding for when the mouse is moving too fast for the framerate to keep up

# Idea: Compare previous mouse position and current mouse position's i's and j's and the ratio of i/j to predict what way the user wants the line to go

def pathfind(dragging, hitbox, prevPoint, grid, colourEmpty):
    if dragging and hitbox.rect.collidepoint(pg.mouse.get_pos()):
        # Checking that the hitbox is empty and not the prevPoint
        if hitbox != prevPoint and hitbox.colour == colourEmpty:
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