import game, menu


def setup():
    global smallFont, font, bigFont, gameStage
    
    smallFont = [16, createFont("Ariel", 16)]
    font = [24, createFont("Ariel", 24)]
    bigFont = [48, createFont("Ariel", 48)]
    gameStage = 0
    
    game.setup()
    
    size(800, 400)

def draw():
    global smallFont, font, bigFont, gameStage
    
    if gameStage == 0:
        menu.draw(font, bigFont)
    else:
        game.draw(smallFont, font, bigFont)
        
def keyTyped():
    global gameStage
    
    if gameStage == 0:
        if menu.keyTyped():
            gameStage = 1
    else:
        if not game.keyTyped():
            gameStage = 0
            game.setup()
    
