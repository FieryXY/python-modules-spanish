# Cuándo este programa está completado, el programa va a dibujar un topo
# en cada agujero

def setup():
     size(400, 400)
     background(78, 166, 51) # verde como el pasto
      
     #Este código dibuja los agujeros. Ejecute el programa para verlos
     fill(0, 0, 0)
     ellipse(200, 200, 100, 30)
     ellipse(70, 119, 100, 30)
     ellipse(300, 60, 100, 30)
     ellipse(297, 350, 100, 30)

def draw():
    #Escriba código aqúi que use dibujar_topo() para poner un topo en cada
    # agujero.


    pass

# =================== DO NOT MODIFY THE CODE BELOW =====================

def dibujar_topo(topo_x, topo_y):
     noStroke()
     fill(125, 93, 43)
     ellipse(topo_x, topo_y, 60, 60) # face
     fill(255, 237, 209)
     ellipse(topo_x, topo_y+10, 33, 28) 
     fill(0, 0, 0)
     ellipse(topo_x-10, topo_y-15, 10, 10) # eyes
     ellipse(topo_x+10, topo_y-15, 10, 10)
     ellipse(topo_x, topo_y-5, 10, 10) # nose
     ellipse(topo_x, topo_y+10, 20, 5) # mouth
