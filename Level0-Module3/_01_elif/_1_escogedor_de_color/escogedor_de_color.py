import random
import turtle
from tkinter import simpledialog

# Devuelve un color aleatorio
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== NO CAMBIE EL CÓDIGO A LA CIMA ===========================

if __name__ == '__main__':
    pantalla = turtle.Screen()
    pantalla.bgcolor('white')

    # TODO 1) Cree una tortuga nueva que se llama "mi_tortuga"
    #       2) Haga que la tortuga dibuja una forma (esta acción se hará en más de una línea de código)
    #       3) Fije el grueso del bolígrafo de su tortuga a 10
    #       4) Pregúntele al usuario que color de bolígrafo quiere que dibuje
    #       5) Use una declaración if/else para fijar el color de bolígrafo que el usuario ha elegido
    #       6) Si el usuario no escribe nada, elija un color aleatorio
    #       7) Ponga un bucle alrededor de su código para que siga preguntándole al usuario que color de bolígrafo quiere que dibuje
    #           y la tortuga siga dibujándolos

    # ===================== NO CAMBIE EL CÓDIGO DEBAJO ============================
    turtle.done()
