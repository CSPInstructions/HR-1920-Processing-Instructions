import functions

def draw(font, largeFont):
    background(0, 100, 0)
    
    functions.drawText(255, 255, 255, largeFont[1], "TypeMania", 400, 200 + largeFont[0] // 2)
    functions.drawText(255, 255, 255, font[1], "Press space to continue", 400, 300 + font[0] // 2)

def keyTyped():
    return key == " "
