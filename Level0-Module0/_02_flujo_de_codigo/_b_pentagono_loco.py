import random
import turtle

#Traducciones Nuevos:
# Esconder - Hide
# Completado - Done

# Da un color aleatorio!
def dar_color_aleatorio():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

def dar_color_proximo(i):
    return colores[i % len(colores)]


# ====================== NO CAMBIE EL CÓDIGO ENCIMA ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('black')
    window.setup(width=0.75, height=0.9, startx=0, starty=0)
    
    colores = ('red', 'blue', 'green', 'yellow', 'orange') #rojo, azul, verde, amarillo, naranja
    
    # Cree una tortuga nueva que se llama "mi_tortuga"

    #Cambie la forma de la tortuga a 'turtle', .shape('turtle')
    
    # Fije la velocidad de la tortuga al máximo (0)
    
    #Fije el ancho a 1

    #Cree una variable para guardar el número de líneas en un pentágono
    
    # Cree una variable a guardar el ángulo de 360 / (variable con número de líneas)
    
    # Use un bucle de for para repetir las siguentes líneas de código 360 veces
        # Si la variable de bucle (x) es igual a 100, fije el ancho de la tortuga a 2

        # Si la variable de bucle (x) es igual a 200, fije el ancho de la tortuga a 3
        
        # Use la función dar_color_proximo a fijar el "pencolor" de la tortuga
            # Pista: .pencolor(dar_color_proximo(i))

        # Doble la tortuga a la derecha por (x+1) grados

    #Esconda su tortuga para que pueda ver la pauta
        # mi_tortuga.hideturtle()
        
    # Compare su pauta con el imagen "PentagonoLoco.png". Si los pautas son iguales, esta actividad está completada
    
    # Variaciones:
        # Hacer la pauta muy grande
        # Cambiar los colores
        # Probar formas diferentes

    #Use la función turtle.done()
    turtle.done()