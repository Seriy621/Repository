x = 0
mode = 1
def setup():
    size(300,300)
    background(0)
def draw():
    global x,mode
    background(0)
    frameRate(100)
    if mousePressed:
       background(0)
       x = 0
    else:
        fill(random(0,255),random(0,255),random(0,255))
        ellipse(x,x,10,10)
    if mode == 1:
        x = x + 1
    if mode == -1:
        x = x - 1
    if x <= 0:
        mode = 1
    if x >= 300:
        mode = -1
    
