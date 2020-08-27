import os
import csv
import operator
import numpy as np
from math import exp, sin, cos, pi
from tkinter import *
from random import randrange as rnd, choice
import time

class Player(object):
    def __init__(self, name, result):
        self.name = name
        self.result = result
table = open('players_table.csv', 'a+', newline = '')

player = Player(str(input()), 0)

root = Tk()

canv = Canvas(root, width = 800, height = 600, bg='black')
canv.pack(fill=BOTH,expand=1)
l = Label(bg='red', fg='white', width=40)
colors = ['pink', 'yellow','lightgreen','lightblue']

class Target(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
        t = np.arange(0, 6*pi, pi/10)
        points = []
        self.fig = []
        for teta in t:
            r = 15
            b = 0.05
            px = (self.x + r*exp(b*teta)*cos(teta))
            py = (self.y + r*exp(b*teta)*sin(teta))
            points.append(px)
            points.append(py)
        Q = np.arange(0, len(points), 4)
        for q in Q:
            l = canv.create_line(points[q],points[q+1],points[q+2],points[q+3], fill = "red", width = 4)
            self.fig.append(l)
    def move_target(self):
        vx = rnd(-20, 20)
        vy = rnd(-20, 20)
        self.x+=vx
        self.y+=vy
        for k in range(len(self.fig)):
            canv.move(self.fig[k], vx, vy)
        root.update()
        
        root.after(10, self.move_target)
    def remove_target(self):
        for l in self.fig: canv.delete(l)
            
            
text = []
i = -1
balls = []
xs = []
ys = []
rs = []
vxs = []
vys = []

j = -1
targets = []
t_xs = []
t_ys = []


def new_ball():
    global i
    
    if i>0 and (i%3 == 0):
        i = -1
        for ball in balls: canv.delete(ball)
        balls.clear()
        xs.clear()
        ys.clear()
        rs.clear()
        vxs.clear()
        vys.clear()
        
    i+=1
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,40)
    xs.append(x)
    ys.append(y)
    rs.append(r)

    vx = rnd(-10, 10)
    vy = rnd(-10, 10)
    vxs.append(vx)
    vys.append(vy)
    
    ball = canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    balls.append(ball)
    
    root.after(2000,new_ball)

def new_target():
    global j
    if (j>1):
        for h in range(len(targets)): targets[h].remove_target()
        j = -1
        targets.clear()
        t_xs.clear()
        t_ys.clear()
        
    j+=1   
    
    x = rnd(100, 700)
    y = rnd(100, 500)
    t_xs.append(x)
    t_ys.append(y)

    t = Target(x, y)
    t.move_target()
    targets.append(t)

    root.after(5000, new_target)
        

def move_ball():
    for k in range(len(balls)):
        xs[k]+= vxs[k]
        ys[k]+= vys[k]
        
        if (abs(xs[k])>= 800 - rs[k]) or xs[k] <= rs[k]: vxs[k] = -vxs[k]
        if (abs(ys[k])>= 600 - rs[k]) or ys[k] <= rs[k]: vys[k] = -vys[k]
        
        canv.move(balls[k], vxs[k], vys[k])
    
    root.update()
    root.after(10, move_ball)
    
    
score = 0

def click(event):
    global score, cl
    canv.create_rectangle(10, 10, 790, 590, outline = 'black', width = 5 )
    for t in text: canv.delete(t)
    for k in range(len(balls)):
        x = xs[k]
        y = ys[k]
        r = rs[k]
        if (((x - event.x)**2 + (y - event.y)**2) <= r**2) and ((i == k) or (i == k-1) or (i == k-2)):
            t = canv.create_text(430, 300, text = "goal", fill = "lightblue" )
            text.append(t)
            canv.create_rectangle(10, 10, 790, 590, outline = 'lightblue', width = 5 )
            score+=1
            l['text'] = score
            
    for k in range(len(targets)):
        x = targets[k].x
        y = targets[k].y
        r = 15*exp(0.05*6*pi)
        if (((x - event.x)**2 + (y - event.y)**2) <= r**2):
            t = canv.create_text(430, 300, text = "BONUS! \n 10 points!", font = "Arial 18" ,fill = "lightgreen" )
            text.append(t)
            canv.create_rectangle(10, 10, 790, 590, outline = 'lightgreen', width = 5 )
            score+=10
            l['text'] = score

new_ball()
move_ball()
new_target()
canv.bind('<Button-1>', click)
l.pack()

mainloop()

player.result = score


with table:
    players = csv.writer(table)
    players.writerow([player.name, str(player.result)])


os.remove("rating_table.csv")
rating_table = open('rating_table.csv', 'a+', newline = '')
players = csv.reader(open('players_table.csv', 'r'))
rating = reversed(sorted(players, key = operator.itemgetter(1)))

r = open('rating_table.csv', 'w', newline = '')
with r:
    rec = csv.writer(r)
    rec.writerows(rating)


