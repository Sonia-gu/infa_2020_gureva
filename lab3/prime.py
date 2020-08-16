from graph import *
import numpy as np
import math
from math import sqrt, sin, cos, pi

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
