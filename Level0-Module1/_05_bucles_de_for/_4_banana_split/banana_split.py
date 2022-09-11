"""
* 1. Look at the image bananasplit.png

* 2. Your mission is to create a python program that recreates that image
     using the create_text function
     
* 3. The catch is, you can only type the create_text function ONE TIME ONLY
     into your program. Using a loop and if-statements, you must figure out
     how to vary the text and the positioning so that you can read all four
     separate lines.
"""

"""
     1. Mire el imagen bananasplit.png

     2. Su meta es crear un programa que recrea este imagen con la función create_text

     3. Solamente puede usar la función create_text UNA VEZ en su programa. Use un bucle y declaraciones de "si"
     para determinar como cambiar el texto y ubicación en el dibujo para crear los 4 líneas
"""

from tkinter import *
import tkinter as tk

root = tk.Tk()

cuadro = tk.Canvas(root, width=200, height=200, bg="#FF00FF");
cuadro.grid()

'''
Ejemplo de Crear Texto:
                    x    y                                                       
cuadro.create_text(100, 50, text="text goes here", font=("Arial", 16))
'''
# Ponga su código debajo


root.mainloop()
