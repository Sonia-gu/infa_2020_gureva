from graph import *
import numpy as np
import math
from math import sqrt, sin, cos, pi

windowSize(700, 700)
canvasSize(700, 700)
viewCoords(-350, 350, -350, 350)

def oval(_x, _y, a, b, color):

    brushColor(color)
    X = np.arange(_x - a, _x + a, 1)
    P = []
    for x in X:
        p = (x , -b*sqrt(1 - ((x-_x)/a)**2) + _y)
        P.append(p)
    for x in reversed(X):
        p = (x , b*sqrt(1 - ((x-_x)/a)**2) + _y)
        P.append(p)

    polygon(P)


#background

brushColor("black")
rectangle(-350, 350, 350, -350)

#body

brushColor("orange")
circle(0, -350, 200)

#face&hands
penColor("pink")
brushColor("pink")
circle(0, 0, 200)
penSize(30)
line(-200, -200, -270, 220)
line(200, -200, 270, 220)
penSize(1)
penColor("white")
circle(-270, 250, 40)
circle(270, 250, 40)

penColor("black")
penSize(1)

#poster

brushColor("lightgreen")
rectangle(-350, 350, 350, 250)
text("PYTHON is AMAZING", 30, 30, font=("Arial", 50))

#t-shirt
brushColor("orange")
t = np.arange(0, 2*pi, 2*pi/5)
hand1 = []
hand2 = []
for i in t:
    p1 = (80*cos(i) - 200, 80*sin(i)-200)
    p2 = (80*cos(i+ pi/5) - 200 + 400, 80*sin(i+ pi/5)-200)
    hand1.append(p1)
    hand2.append(p2)
polygon(hand1)
polygon(hand2)

#eyes

oval(70, 20, 45, 35, "lightblue")
oval(-70, 20, 45, 35, "lightblue")
oval(-70, 20, 15, 10, "black")
oval(70, 20, 15, 10, "black")

#nose&mouth

points1 = [(-25, -20), (25, -20), (0, -45)]
points2 = [(-70, -60), (70, -60), (0, -100)]
brushColor("brown")
polygon(points1)
brushColor("red")
polygon(points2)

#hair

brushColor("purple")
tr = np.arange(pi/4, 3*pi/4, pi/20)
for i in tr:
    pp = [((200+60)*cos(i), (200+60)*sin(i)) , (200*cos(i) + 30*sin(i) ,200*sin(i) - 30*cos(i) ), (200*cos(i)-30*sin(i),200*sin(i) + 30*cos(i) )]
    polygon(pp)

run()
