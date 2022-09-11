import random
import turtle




# Da un color aleatorio!
def dar_color_aleatorio():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

def dar_color_proximo(i):
    return colores[i % len(colores)]

# ====================== NO CAMBIE EL CÓDIGO ENCIMA ===========================


if __name__ == '__main__':
    window = turtle.Screen()
    colores = ['red', 'blue', 'green', 'yellow', 'orange'] #rojo, azul, verde, amarillo, naranja

    talla_centro = 200        # La talla del centro negro de la estrella
    talla_fuego = 130         # El largo de los brazos de fuego de la estrella
    
    # Cree una tortuga nueva que se llama "mi_tortuga"
    
    # Cambie la forma de la tortuga a 'turtle', .shape('turtle')
    
    # Fije el ancho de la tortuga a 2
    
    # Fije la velocidad de la tortuga a 0 (más rápido)

    # Use un "for loop" para repetir el código debajo UNA vez (vamos a cambiar este número luego)

        # Fije .fillcolor() de la tortuga a naranja (Color de Relleno = fill color)

        # Use la función .begin_fill()

        # DOBLE A LA DERECHA       Doble la tortuga 1/8 de un círculo (Pista: Un círculo completo es 360 grados)

        # DIBUJE                    Mueva la tortuga 64 píxeles

        # DOBLE A LA IZQUIERDA      Doble la tortuga 40 grados a la IZQUIERDA (izquierda = left)

        # DIBUJE EL FUEGO           Mueva la tortuga la distancia de talla_fuego

        #                           Doble la tortuga 170 grados a la derecha

        #                           Mueva la tortuga la distance de talla_fuego otra vez

        # DOBLE A LA DERECHA        Doble la tortuga 62 grados a la derecha

        # DIBUJE                    Mueva la tortuga la distancia de talla_centro

        # Use la función .end_fill()
        
    # Esconda la tortuga para que pueda ver la pauta

    # PRUEBA    Ejecute el programa. Verifique que la forma sea igual al imagen "EstrellaDeFuego.png" pero con
    #           solamente un brazo de la estrella. No se preocupe sobre los colores.

    #COLOR      Cambie el color de pencolor de la tortuga para que el fuego sea un color
    #           diferente al resto de la estrella. Ejecute el programa otra vez y verificar los cambios.

    # BUCLE     Cuándo un brazo se ve correcto, cambie su bucle a repetir 25 veces

    # Use la función .done()
    turtle.done()