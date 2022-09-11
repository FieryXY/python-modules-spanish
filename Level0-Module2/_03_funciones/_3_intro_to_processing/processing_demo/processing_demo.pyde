"""
Processing Demo
"""


#Processing tiene muchas funciones para dibujar formas coloridas
#Es muy fácil! Vamos a hacer un ejemplo:
def setup():
    #Setup significa establecer (construir la pantalla)

    #La función size(ancho, altura) crea una pantalla con
    #las dimensiones especificadas
    size(800, 600)


def draw():
    #Draw significa Dibujar
    # background() selecciona el color del fondo.
    #En este caso, "#FFFFFF' es blanco
    background('#FFFFFF')

    # fill() elige un color. En este caso, '#0000FF' es azul
    # Puede crear su propio color con Tools -> Color Selector
    fill('#0000FF')

    # ellipse() dibuja una elipse. Los parámetros son x,y,ancho, altura
    #mouseX y mouseY representan "x" y "y" del cursor en la pantalla.
    #Esta línea de código dibuja una elipse alrededor del cursor
    ellipse(mouseX, mouseY, 100, 100)

    #El código debajo prueba si el ratón está apretado. Si está,
    #dibuja una elipse roja encima de la azul

    if mousePressed: #mousePressed significa ratonApretado
        fill('#FF0000')
        ellipse(mouseX, mouseY,  100,   100)

    # TODO: Crea otras formas con tallas y colores diferentes
    rect(x,y,ancho altura) #Rectángulo
    triangle(x1,y1,x2,y2,x3,y3) #Triángulo con los tres ubicaciones especificadas
    
