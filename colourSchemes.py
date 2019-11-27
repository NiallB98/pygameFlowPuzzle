from random import shuffle

alpha = 0.25
numColours = 16

def transparent(clr, t):
    
    (redPart, greenPart, bluePart) = clr
    
    redPart = int(round(redPart * t))
    greenPart = int(round(greenPart * t))
    bluePart = int(round(bluePart * t))
    return (redPart, greenPart, bluePart)

class colourScheme:
    
    def __init__(self, scheme='default'):
        
        COLOUR = {}
        self.lineColour = {}
        self.colour = {}
        
        if scheme == 'default':
            
            COLOUR[0] = (150, 0, 0) # Red
            COLOUR[1] = (0, 0, 150) # Blue
            COLOUR[2] = (150, 150, 0) # Yellow
            COLOUR[3] = (0, 150, 0) # Green
            COLOUR[4] = (0, 150, 150) # Teal
            COLOUR[5] = (150, 0, 150) # Magenta
            COLOUR[6] = (150, 150, 150) # Grey
            COLOUR[7] = (74, 232, 38) # Lime
            COLOUR[8] = (199, 167, 255) # Lilac
            COLOUR[9] = (255, 119, 12) # Orange
            COLOUR[10] = (255, 51, 120) # Pink
            COLOUR[11] = (26, 31, 107) # Navy
            COLOUR[12] = (26, 99, 0) # Dark Green
            COLOUR[13] = (255, 113, 103) # Peach
            COLOUR[14] = (121, 177, 255) # Light Blue
            COLOUR[15] = (121, 255, 160) # Light Green
            
            for i in range(0, numColours):
                self.lineColour[i] = COLOUR[i]
            shuffle(self.lineColour)
            
            for i in range(0, numColours):
                self.colour[i] = transparent(self.lineColour[i], alpha)
            
        else:
            
            COLOUR[0] = (150, 0, 0) # Red
            COLOUR[1] = (0, 0, 150) # Blue
            COLOUR[2] = (150, 150, 0) # Yellow
            COLOUR[3] = (0, 150, 0) # Green
            COLOUR[4] = (0, 150, 150) # Teal
            COLOUR[5] = (150, 0, 150) # Magenta
            COLOUR[6] = (150, 150, 150) # Grey
            COLOUR[7] = (74, 232, 38) # Lime
            COLOUR[8] = (199, 167, 255) # Lilac
            COLOUR[9] = (255, 119, 12) # Orange
            COLOUR[10] = (255, 51, 120) # Pink
            COLOUR[11] = (26, 31, 107) # Navy
            COLOUR[12] = (26, 99, 0) # Dark Green
            COLOUR[13] = (255, 113, 103) # Peach
            COLOUR[14] = (121, 177, 255) # Light Blue
            COLOUR[15] = (121, 255, 160) # Light Green
            
            for i in range(self.lineColour):
                self.lineColour[i] = COLOUR[i]
            shuffle(self.lineColour)
            
            for i in range(self.lineColour):
                self.colour[i] = transparent(self.lineColour[i], alpha)