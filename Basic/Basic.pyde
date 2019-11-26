def setup():
    # Processing klaarmaken voor gebruik
    global bigFont, counter
    
    bigFont = createFont("Helvetica", 80)
    counter = 0
    
    size(400, 600)

def draw():
    # Het tekenen van het scherm
    # Gebeurd 1x per afbeelding
    if counter % 5 == 0:
        background(255, 20, 147)
    else:
        background(0, 200, 0)
    
    # Op het moment dat:
    # beginX < mouseX and mouseX < beginX + width
    
    if 50 < mouseX < 350 and 50 < mouseY < 550:
        fill(150, 0, 150)
    else:
        fill(200, 0, 200)
        
    rect(50, 50, 300, 500)
    
    # print(str(mouseX) + ", " + str(mouseY))
    fill(255, 255, 255)
    textFont(bigFont)
    
    if counter == 0:
        text("Hello", 200, 300)
    else:
        text(counter, 200, 300)
    
    
    textAlign(CENTER)
    
def mousePressed():
    global counter
    
    if mouseButton == LEFT:
        if 50 < mouseX < 350 and 50 < mouseY < 550:
            counter = counter + 1    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
