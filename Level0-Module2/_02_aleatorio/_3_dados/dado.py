"""
    Use un objecto de Random para generar números aleatorios para que su código
    pueda crear números diferentes en un dado
"""
import tkinter as tk
from PIL import Image, ImageTk
import random



def elegir_imagen_aleatorio_de_dado():
    imagen_aleatorio = None #None = Nada

    # TODO Ejecute el código y haga clic en el botón. Observe que solamente un lado del dado
    #   está mostrado.

    # TODO Cambie la línea del código debajo a un número aleatorio generado entre 1 a 6
    #   (incluyendo 1 y 6)
    num_aleatorio = 1

    if num_aleatorio == 1:
        imagen_aleatorio = crear_imagen('dado 1.png', 400, 400)
    elif num_aleatorio == 2:
        imagen_aleatorio = crear_imagen('dado 2.png', 400, 400)
    elif num_aleatorio == 3:
        imagen_aleatorio = crear_imagen('dado 3.png', 400, 400)
    elif num_aleatorio == 4:
        imagen_aleatorio = crear_imagen('dado 4.png', 400, 400)
    elif num_aleatorio == 5:
        imagen_aleatorio = crear_imagen('dado 5.png', 400, 400)
    elif num_aleatorio == 6:
        imagen_aleatorio = crear_imagen('dado 6.png', 400, 400)
    else:
        print("ERROR: Número Aleatorio Inválido")

    return imagen_aleatorio

# ======================= NO CAMBIE EL CÓDIGO DEBAJO =========================


def crear_imagen(nombre_de_fichero, ancho, altura):
    imagen_obj = None

    try:
        imagen = Image.open(nombre_de_fichero)
        imagen = imagen.resize((ancho, altura), Image.ANTIALIAS)
        imagen_obj = ImageTk.PhotoImage(image=imagen)
    except FileNotFoundError as fnf:
        print("ERROR: Unable to find file " + filename)

    return image_obj


class Dado(tk.Tk):

    def __init__(self):
        super().__init__()

        imagen_aleatorio = elegir_imagen_aleatorio_de_dado()
        self.label_imagen = tk.Label(self, image=imagen_aleatorio)
        self.label_imagen.imagen = imagen_aleatorio
        self.label_imagen.pack()

        self.boton = tk.Button(self, text='Rodar!', command=self.boton_clic)
        self.boton.pack()

    def boton_clic(self):
        imagen_aleatorio = elegir_imagen_aleatorio_de_dado()
        self.label_imagen.config(image=imagen_aleatorio)
        self.label_imagen.imagen = imagen_aleatorio


if __name__ == '__main__':
    # Create a new object of the class
    app = Dado()
    app.title('Simulador de Dado') #Título

    # Sets the size of the app window
    app.geometry('500x450')

    app.mainloop()

