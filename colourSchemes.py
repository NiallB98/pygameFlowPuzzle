alpha = 0.2

def transparent(clr, t):
    
    (redPart, greenPart, bluePart) = clr
    
    redPart = int(round(redPart * t))
    greenPart = int(round(greenPart * t))
    bluePart = int(round(bluePart * t))
    return (redPart, greenPart, bluePart)

class colourScheme:
    
    def __init__(self, scheme):
        
        self.colour = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
        self.lineColour = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
        
        if scheme == 'default':
            
            COLOUR1 = (150, 0, 0) # Red
            COLOUR2 = (0, 0, 150) # Blue
            COLOUR3 = (150, 150, 0) # Yellow
            COLOUR4 = (0, 150, 0) # Green
            COLOUR5 = (0, 150, 150) # Teal
            COLOUR6 = (150, 0, 150) # Magenta
            COLOUR7 = (150, 150, 150) # Grey
            COLOUR8 = (74, 232, 38) # Lime
            COLOUR9 = (199, 167, 255) # Lilac
            COLOUR10 = (255, 119, 12) # Orange
            COLOUR11 = (255, 51, 120) # Pink
            COLOUR12 = (26, 31, 107) # Navy
            COLOUR13 = (26, 99, 0) # Dark Green
            COLOUR14 = (255, 113, 103) # Peach
            COLOUR15 = (121, 177, 255) # Light Blue
            COLOUR16 = (121, 255, 160) # Light Green
            
            self.colour[0] = transparent(COLOUR1, alpha) # 1st Colour - Red
            self.lineColour[0] = COLOUR1
            self.colour[1] = transparent(COLOUR2, alpha) # 1st Colour - Red
            self.lineColour[1] = COLOUR2
            self.colour[2] = transparent(COLOUR3, alpha) # 1st Colour - Red
            self.lineColour[2] = COLOUR3
            self.colour[3] = transparent(COLOUR4, alpha) # 1st Colour - Red
            self.lineColour[3] = COLOUR4
            self.colour[4] = transparent(COLOUR5, alpha) # 1st Colour - Red
            self.lineColour[4] = COLOUR5
            self.colour[5] = transparent(COLOUR6, alpha) # 1st Colour - Red
            self.lineColour[5] = COLOUR6
            self.colour[6] = transparent(COLOUR7, alpha) # 1st Colour - Red
            self.lineColour[6] = COLOUR7
            self.colour[7] = transparent(COLOUR8, alpha) # 1st Colour - Red
            self.lineColour[7] = COLOUR8
            self.colour[8] = transparent(COLOUR9, alpha) # 1st Colour - Red
            self.lineColour[8] = COLOUR9
            self.colour[9] = transparent(COLOUR10, alpha) # 1st Colour - Red
            self.lineColour[9] = COLOUR10
            self.colour[10] = transparent(COLOUR11, alpha) # 1st Colour - Red
            self.lineColour[10] = COLOUR11
            self.colour[11] = transparent(COLOUR12, alpha) # 1st Colour - Red
            self.lineColour[11] = COLOUR12
            self.colour[12] = transparent(COLOUR13, alpha) # 1st Colour - Red
            self.lineColour[12] = COLOUR13
            self.colour[13] = transparent(COLOUR14, alpha) # 1st Colour - Red
            self.lineColour[13] = COLOUR14
            self.colour[14] = transparent(COLOUR15, alpha) # 1st Colour - Red
            self.lineColour[14] = COLOUR15
            self.colour[15] = transparent(COLOUR16, alpha) # 1st Colour - Red
            self.lineColour[15] = COLOUR16
            
        else:
            
            COLOUR1 = (150, 0, 0) # Red
            COLOUR2 = (0, 0, 150) # Blue
            COLOUR3 = (150, 150, 0) # Yellow
            COLOUR4 = (0, 150, 0) # Green
            COLOUR5 = (0, 150, 150) # Teal
            COLOUR6 = (150, 0, 150) # Magenta
            COLOUR7 = (150, 150, 150) # Grey
            COLOUR8 = (74, 232, 38) # Lime
            COLOUR9 = (199, 167, 255) # Lilac
            COLOUR10 = (255, 119, 12) # Orange
            COLOUR11 = (255, 51, 120) # Pink
            COLOUR12 = (26, 31, 107) # Navy
            COLOUR13 = (26, 99, 0) # Dark Green
            COLOUR14 = (255, 113, 103) # Peach
            COLOUR15 = (121, 177, 255) # Light Blue
            COLOUR16 = (121, 255, 160) # Light Green
            
            self.colour[0] = transparent(COLOUR1, alpha) # 1st Colour - Red
            self.lineColour[0] = COLOUR1
            self.colour[1] = transparent(COLOUR2, alpha) # 1st Colour - Red
            self.lineColour[1] = COLOUR2
            self.colour[2] = transparent(COLOUR3, alpha) # 1st Colour - Red
            self.lineColour[2] = COLOUR3
            self.colour[3] = transparent(COLOUR4, alpha) # 1st Colour - Red
            self.lineColour[3] = COLOUR4
            self.colour[4] = transparent(COLOUR5, alpha) # 1st Colour - Red
            self.lineColour[4] = COLOUR5
            self.colour[5] = transparent(COLOUR6, alpha) # 1st Colour - Red
            self.lineColour[5] = COLOUR6
            self.colour[6] = transparent(COLOUR7, alpha) # 1st Colour - Red
            self.lineColour[6] = COLOUR7
            self.colour[7] = transparent(COLOUR8, alpha) # 1st Colour - Red
            self.lineColour[7] = COLOUR8
            self.colour[8] = transparent(COLOUR9, alpha) # 1st Colour - Red
            self.lineColour[8] = COLOUR9
            self.colour[9] = transparent(COLOUR10, alpha) # 1st Colour - Red
            self.lineColour[9] = COLOUR10
            self.colour[10] = transparent(COLOUR11, alpha) # 1st Colour - Red
            self.lineColour[10] = COLOUR11
            self.colour[11] = transparent(COLOUR12, alpha) # 1st Colour - Red
            self.lineColour[11] = COLOUR12
            self.colour[12] = transparent(COLOUR13, alpha) # 1st Colour - Red
            self.lineColour[12] = COLOUR13
            self.colour[13] = transparent(COLOUR14, alpha) # 1st Colour - Red
            self.lineColour[13] = COLOUR14
            self.colour[14] = transparent(COLOUR15, alpha) # 1st Colour - Red
            self.lineColour[14] = COLOUR15
            self.colour[15] = transparent(COLOUR16, alpha) # 1st Colour - Red
            self.lineColour[15] = COLOUR16