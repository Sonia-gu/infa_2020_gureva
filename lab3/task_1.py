from graph import *
(width, height) = windowSize()
print((width, height))


brushColor("yellow")
circle(250,300, 120)

brushColor("red")
circle(200, 275, 25)
circle(300, 275, 20)

brushColor("black")
circle(200, 275, 10)
circle(300, 275, 10)
rectangle(190, 360, 310, 380)

penSize(15)
line(130, 210, 240, 260)
line(270, 260, 370, 220)


run()
