#Bienvenidos a la introducción de programación! Esta carpeta contiene 13 lecciones. Después de completarlas, podrás crear programas en Python!
#Python es un idioma de programación común en muchos trabajos

#Para empezar, vamos a usar La Tortuga de Python para aprender los básicos.
#Haz click en el triángulo para ejectuar el código cuando necesitas.


#Español a Inglés Traducciones para esta lección:
# Tortuga - Turtle
# Forma - Shape
# Velocidad - Speed
# Color de Perímetro - Pen Color o pencolor
# Adelante - Forward
# Izquierda - Left
# Derecha - Right
# Ir a - Go To o goto
# Pasos - steps
# Empezar a Llenar - Begin Fill (begin_fill)
# Dejar de Llenar - End Fill (end_fill)
# Verde - Green
# Azul - Blue

import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # Este código crea una tortuga nueva. Cambia el nombre de la tortuga! Ahora, el nombre es "mi_tortuga"
    mi_tortuga = turtle.Turtle()

    #EJECUTE EL CÓDIGO. ¿Ves la tortuga?

    #Cambie la forma de su tortuga para parecerse a una tortuga. Usa [nombre de su tortuga].shape('turtle')

    #Cambie la velocidad de su tortuga a 2 con .speed(2)

    #Cambie el color de su tortuga con .color('green') y .pencolor('blue')

    #Diga su tortuga a caminar adelante con .forward(100)

    #PRUEBA (Ejecute su Código)   ¿Mueve su Tortuga?

    #Diga su tortuga a doblar con .left(90) o .right(90). El número es el número de grados a doblar

    #Ahora, ponga su código de adelante y izquierda/derecha en un "for loop" para repetirlo 4 veces
    for i in range(4):
        print("Dibujando un Borde...")
        #Ponga su código aquí

    #PRUEBA Su tortuga dibuja un cuadrado?

    #Se puede mover su tortuga a una ubicación nueva en la pantalla con la función .goto(x,y). x=0 y y=0 es el centro de la pantalla
    #Mueva su tortuga a una ubicación nueva

    #Dibuje un círculo con su tortuga con .circle(radius, steps=30). Reempleze "radius" con el radio del círculo.

    # PRUEBA ¿Su tortuga dibujó un círculo?

    #Ponga un color de relleno en su forma por añadir .begin_fill() antes de dibujar el círculo y .end_fill() después de dibujar el círculo

    #Use su conocimiento nuevo para crear 3 formas más con colores de relleno diferentes

    # ===================== NO CAMBIE EL CÓDIGO DEBAJO ============================
    turtle.done()