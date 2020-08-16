from prime_figures import *

windowSize(500, 700)
canvasSize(500, 700)
viewCoords(-250, 250, -350, 350)
 
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

alien(-110, -60, 100, -1)
alien(-100, -250, 150, -1)
alien(-80, -150, 120, 1)
alien(-180, -150, 120, -1)
alien(120, -150, 300, 1)

UFO(-110, 70, 110)
UFO(150, 80, 80)
UFO(-30, 20, 40)
  
run()
