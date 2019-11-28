import pygame as pg

class squares(pg.sprite.Sprite):
    
    def __init__(self, x, y, colour, lineColour, dx, i, j, win):
        pg.sprite.Sprite.__init__(self)
        
        self.x = x
        self.y = y
        self.i = i
        self.j = j
        
        self.colour = colour
        self.lineColour = lineColour
        
        super(pg.sprite.Sprite, self).__init__()
        self.rect = pg.Rect(self.x, self.y, dx - 3, dx - 3)
    
    # Drawing Self
    def drawSq(self, win, dx, colour=None):
        if colour == None:
            colour = self.colour
        pg.draw.rect(win, colour, (self.x, self.y, dx, dx))
        
    # Drawing Source Circle
    def drawCirc(self, win, dx):
        radius = round(dx / 12) * 3
        centrex = round(self.x + (dx / 2)) - 1
        centrey = round(self.y + (dx / 2)) - 1
        pg.draw.circle(win, self.lineColour, (int(centrex), int(centrey)), int(radius))