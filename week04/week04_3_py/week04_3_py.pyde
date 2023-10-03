def setup():
    size(500,500)
def draw():
    background(0) # 黑色的背景
    for i in range(frameCount):
        a, a2 = i/36.0, i/36.0*365/88
        stroke(255) #白色的線
        line(250+200*cos(a), 250+200*sin(a), 250+79*cos(a2), 250+79*sin(a2))
    
    fill(229, 189, 53) 
    ellipse(250,250, 80,80) # 太陽
    a, a2 = frameCount/36.0, frameCount/36.0*365/88
    ellipse(250+200*cos(a), 250+200*sin(a), 10, 10) #地球
    ellipse(250+79*cos(a2), 250+79*sin(a2), 10, 10) #水星
