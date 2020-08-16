from graph import *
import numpy as np
import math
from math import sqrt, sin, cos, pi
windowSize(500, 700)
canvasSize(500, 700)
viewCoords(-250, 250, -350, 350)

def sect(c_x, c_y ,start, R, phi, color, pcolor):
    brushColor(color)
    penColor(pcolor)
    ang = np.arange(start, start+phi, phi/200)
    P = [(c_x, c_y), (c_x + R*cos(start), c_y + R*sin(start))]
    for an in ang:
        x = c_x + R*cos(an)
        y = c_y + R*sin(an)
        p = (x , y)
        P.append(p)
    return polygon(P)

class Oval(object):
    def __init__(self, _x, _y, a, b, color, line):
        self.x = _x
        self.y = _y
        self.a = a
        self.b = b
        self.color = color
        penColor(line)
        
    def fig(self):
        brushColor(self.color)
        X = np.arange(self.x - self.a, self.x + self.a, 1)
        P = []
        for x in X:
            p = (x , -self.b*sqrt(abs(1 - ((x - self.x)/self.a)**2)) + self.y)
            P.append(p)
        for x in reversed(X):
            p = (x , self.b*sqrt(abs(1 - ((x-self.x)/self.a)**2)) + self.y)
            P.append(p)

        return polygon(P)        
    def y_p(self, x):
        return self.b*sqrt(abs(1 - ((x-self.x)/self.a)**2)) + self.y
    def elips(self, line):
        penColor(self.color)
        X = np.arange(self.x - self.a, self.x + self.a, self.a/20)
        moveTo(self.x - self.a, self.y)
        for x in X : point(x, self.y_p(x))
        for x in reversed(X) : point(x, -self.y_p(x) + 2*self.y)

            

class Sect(object):
    def __init__(self, c_x, c_y , R, start, phi, color, pcolor):
        self.center = (c_x, c_y)
        self.startp = (c_x + R*cos(start), c_y + R*sin(start))
        self.finishp = (c_x + R*cos(start+phi), c_y + R*sin(start+phi))
        self.fig = sect(c_x, c_y ,start, R, phi, color, pcolor)
            

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

                            #building    
 #background   
brushColor(20, 20, 55)
rectangle(-500, 500, 500, -200)
brushColor(0, 100, 0)
rectangle(-500, -50, 500, -500)
Oval(120, 150, 80, 70, "white" , "white").fig()

I =np.arange(0, 350, 70 )
for i in I:
    cloud(-150, i, 300, 50)


I =np.arange(0, 350, 70 )
for i in I:
    cloud(150, i, 250, 200)
    cloud(125, i-50, 300, 50)

    

#objects
alien(-110, -60, 100, -1)
alien(-100, -250, 150, -1)
alien(-80, -150, 120, 1)
alien(-180, -150, 120, -1)
alien(120, -150, 300, 1)

UFO(-110, 70, 110)
UFO(150, 80, 80)
UFO(-30, 20, 40)



#UFO(0, 0, 100)   
run()
