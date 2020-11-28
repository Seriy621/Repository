x = 0
y = 0
def setup():
    size(500,500)
def draw():
    fill(random(0,255),random(0,255),random(0,255))
    global x, y
def keyPressed():
    global x, y
    if key == CODED:
        if keyCode == UP:
            y = y - 10
        if keyCode == DOWN:
            y = y + 10
        if keyCode == RIGHT:
            x = x + 10
        if keyCode == LEFT:
            x = x - 10
    rect(x,y,10,10)
        

    

    
    
            
            
        
        
    
