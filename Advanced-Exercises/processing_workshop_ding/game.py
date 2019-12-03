import functions

def resetGame():
    global words, currentWord, currentEntry, corrects, errors
    
    currentWord = words[int(random(len(words)))]
    currentEntry = ""
    
def checkVictory():
    global currentWord, currentEntry, corrects
    
    if currentWord == currentEntry:
        corrects = corrects + 1
        resetGame()        

def drawBoard():
    background(240)
    fill(0, 100, 0)
    rect(-10, 300, width + 20, 110)
    
def drawWords(smallFont, font, largeFont):
    global currentWord, currentEntry, corrects, errors
    
    functions.drawText(0, 150, 0, smallFont[1], "Type the word or press 0 to quit", 400, 25 + smallFont[0] // 2)
    functions.drawText(0, 150, 0, largeFont[1], currentWord, 400, 150 + largeFont[0] // 2)
    functions.drawText(255, 255, 255, font[1], currentEntry, 400, 350 + font[0] // 2) 
    
    score = "words: %d mistakes: %d" % (corrects, errors)
    functions.drawText(255, 255, 255, smallFont[1], score, 400, 375 + smallFont[0] // 2)

def setup():
    global words, corrects, errors

    words = ["huis", "dier", "computer", "programmeren", "code", "python", "processing", "koelkast"]
    corrects = 0
    errors = 0
    
    resetGame()
    
def draw(smallFont, font, largeFont):
    drawBoard()
    drawWords(smallFont, font, largeFont)
    
def keyTyped():
    global currentWord, currentEntry, errors
    
    if key == currentWord[len(currentEntry)]:
        currentEntry = currentEntry + key
        
        checkVictory()
    elif key == "0":
        return False
    else:
        errors = errors + 1
        
    return True
    
