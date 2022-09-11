from tkinter import *
import tkinter as tk

ancho_pantalla = 600
altura_pantalla = 600

root = tk.Tk()

cuadro = tk.Canvas(root, width=ancho_pantalla, height=altura_pantalla, bg="#DDDDDD")
cuadro.grid()

# 1. Pídale al usuario el color de tomate que quiere y guárdela su respuesta
#   Como máximo, provea 3 opciones

# 2. Use if-elif-else cadenas para dibujar el tomate en el color que elegió el ususario.
#   Puede cambiar el código debajo o dibujar su propio tomate

cuadro.create_oval(75, 200, 400, 450, fill="red", outline="")
cuadro.create_oval(200, 200, 525, 450, fill="red", outline="")

cuadro.create_rectangle(275, 100, 325, 230, fill="green", outline="")

root.mainloop()
