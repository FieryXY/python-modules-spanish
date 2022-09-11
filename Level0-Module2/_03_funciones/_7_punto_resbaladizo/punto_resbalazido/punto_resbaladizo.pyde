import math

#Cuándo este programa está completado, el programa va a dibujar
# una elipse que mueve a una ubicación nueva cuándo el usuario haga clic en ella

# 1. Cree 3 variables para representar x,y, y talla de la elipse


def setup():
    # 2. Fije la talla de su cuadro usando la función size(ancho, altura)
    
    pass
     
def draw():

    # 3. Fije el color del fondo de su cuadro

    # 4. Dibuje una elipse usando las variables que ha creadas a la cima
    #   del fichero para la ubicación y talla de su elipse.
    #   Asegure que la elipse fije en la pantalla. Cambie
    #   las variables si no.
    
    pass


# Esta función es usada automáticamente cúando el ratón esté apretado
def mousePressed():
    # 5. Cambie estas variables a los nombres de "x" y "y" del paso #1
    global x
    global y

    # 6. La función distancia_del_cursor(x,y) debajo da un número.
    #   Fije el valor de su variable de distancia al valor recibido
    #   por distancia_del_cursor. Necesita dar esta función la ubicación de su
    #   elipse.


    # 7. Use una declaración de "si" para probar si la variable de distancia es
    #   menor que el radio de la elipse. Si es, fije valores nuevos para
    #   "x" y "y" para una ubicación aleatoria nueva en la pantalla
    #   Pista: x = random(ancho)

    
# ========  Este función da el número de píxeles entre =========
#                    el ratón y el punto (x,y) 
def distancia_del_cursor(x, y):
    return math.sqrt(math.pow((mouseX-x),2) + math.pow((mouseY-y),2))
    
