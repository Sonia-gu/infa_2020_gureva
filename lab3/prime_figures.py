from prime import *

def UFO(x, y, a):    
    A = np.arange(y, y - 2*a , -1.5*a/40)
    for i in A:
        penSize(0)
        penColor("white")
        line(-(i- y)/1.5 + x , i, (i- y)/1.5 + x , i)
    o1 = Oval(x, y, a, a/3, "grey", "grey")
    o2 = Oval(x, y+ a/6, a/1.5, a/4.5, "lightgrey", "lightgrey" )
    o1.fig()
    o2.fig()
    I = np.arange(x - 0.8*a, x + a, 0.8*a/3)
    for i in I:
        Oval(i, y + a/4 - a/2.4*sqrt(1 - (( i - x )/a)**2), a/8, a/24, "white", "white").fig()

def alien(x, y, size, orientation: 1 or -1):
    o = orientation
    col1 = "lightgreen"
    #face
    if o == 1 :s1 = Sect(x, y, size/4, -pi/4, pi/3.8, col1, col1)
    else: s1 = Sect(x, y, size/4, pi, pi/3.8, col1, col1)
    s1.fig
    if o == 1 :s2 = Sect(s1.startp[0], s1.startp[1], size/5.1, 3*pi/8, pi/4, col1, col1)
    else: s2 = Sect(s1.finishp[0], s1.finishp[1], size/5.1, 3*pi/8, pi/4, col1, col1)
    s2.fig
    circle(x + o*size/30, y-size/40, size/25)
    circle(x + o*size/7.6, y- size/6, size/22)
    if o == 1: s3 = Sect(s1.finishp[0], s1.finishp[1], size/4, 14*pi/13, pi/4, col1, col1)
    else: s3 = Sect(s1.startp[0], s1.startp[1], size/4, -pi/13 - pi/4, pi/4, col1, col1)
    brushColor("black")
    circle(x+o*1.2*size/15, y - size/15, size/25)
    circle(x+o*3*size/15, y - size/15, size/30)
    brushColor("white")
    penColor("black")
    circle(x+o*1.2*size/15 + size/150, y - size/15 - size/150, size/120)
    circle(x+o*3*size/15 + size/150, y - size/15 - size/150, size/120)

    
    body = Oval(x+o*size/10, y - size/3, size/16, size/8, col1, "black")
    body.fig()
    #lowerbody
    leg1_1 = Oval(x+ o*size/20, y - (13*size/30), size/35, size/16, col1, col1)
    leg1_2 = Oval(x+ o*size/23, y - size/2, size/50, size/16, col1, col1)
    leg1_1.fig()
    leg1_2.fig()
    brushColor(col1)
    circle(x+ o*size/80, y - size/1.83, size/43)
    leg1_1 = Oval(x+ o*(3*size/20), y - (13*size/30), size/35, size/16, col1, col1)
    leg1_2 = Oval(x+ o*(size/23 + size/9), y - size/2, size/50, size/16, col1, col1)
    leg1_1.fig()
    leg1_2.fig()
    brushColor(col1)
    circle(x+ o*(size/80 + size/6.5), y - size/1.83, size/43)
    #upperbody
    circle(x + o*size/30, y-size/4.5, size/30)
    Oval(x + o*size/90, y-size/3.7, size/30, size/60, col1, col1).fig()
    Oval(x, y-size/3, size/80, size/40, col1, col1).fig()
    circle(x + o*size/30 + o*size/7, y-size/4.5-size/60, size/30)
    Oval(x + o*size/90 + o*size/4.75, y-size/3.7, size/30, size/65, col1, col1).fig()
    Oval(x + o*size/90 + o*size/4, y-size/3.25, size/30, size/60, col1, col1).fig()
    brushColor("red")
    penColor("black")
    circle(x +o*size/3.5, y-size/3.5, size/25)
    Oval(x +o*size/3.5, y-size/4, size/150 ,size/50, "green", "green").fig()
    #antennas
    brushColor(col1)
    penColor(col1)
    for i in range(3):
        circle(x+o*size/4+o*i*size/20, y+size/50+i*size/20, size/80+i*size/80)
    for i in range(3):
        circle(x - o*i*size/20, y+size/50+i*size/20, size/80+i*size/80)

def cloud(c_x, c_y, size, color):
    el = np.arange(1, size, size/20)
    i = color
    for e in el:
        i+=1
        Oval(c_x, c_y, e, e/8, (3*i, 3*i, 3*i), (4*i, 4*i, 4*i)).elips((i, i, i))

