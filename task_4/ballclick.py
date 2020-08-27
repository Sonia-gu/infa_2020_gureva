from tkinter import *
from random import randrange as rnd, choice
import time

root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)
l = Label(bg='red', fg='white', width=40)

colors = ['red','orange','yellow','green','blue']

def new_ball():
    global x,y,r
    canv.delete(ALL)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    
    vx = rnd(10,50)
    vy = rnd(10,50)

    ball = canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)

    while (0<=x<=800) and (0<=y<=600):
        canv.move(ball, vx, vy)
    if(x>=800-2*r):
        while (0<=x<=800-2*r) and (0<=y<=600-2*r):
            canv.move(ball, -vx, vy)
        	
    if(y>=600-2*r):
        while (0<=x<=800-2*r) and (0<=y<=600-2*r):	        
            canv.move(ball, vx, -vy)
            
    root.after(6000,new_ball)

score = 0	

def counter(event):
    global score
    if ((x - event.x)**2 + (y - event.y)**2) <= r:
    	
    	score+=1
    	l['text'] = score
    else:
        l['text']='fail'
        l['text'] = score 


new_ball()
canv.bind('<Button-1>', counter)
l.pack()


mainloop()
