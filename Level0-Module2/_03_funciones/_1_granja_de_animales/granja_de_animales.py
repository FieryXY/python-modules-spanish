import tkinter as tk
from tkinter import simpledialog, Tk
from PIL import Image, ImageTk
from playsound import playsound

pantalla = None

def animales():
    global pantalla
    pantalla = Tk()
    pantalla.withdraw()

    # TODO 1. Pida al usuario el animal que quiere. Entonces, haga el imagen y
    #   sonido del animal con una de las funciones debajo 

    # TODO 2. Escriba el programa para que el usuario pueda seguir pedir animales

    # TODO 3. Si el usuario entra 'salir', pare el programa


# ======================= NO CAMBIE EL CÓDIGO DEBAJO =========================

def mostrar_imagen(filename=None):
    try:
        imagen = Image.open(filename)
    except FileNotFoundError as fnf:
        print("ERROR: Unable to find file " + filename)
        return

    #Ponga el imagen en la pantalla Tk usada por simpledialog para que cuando
    #la pantalla con el imagen está cerrada, el programa mueva al próximo línea del
    #código
    global pantalla
    pantalla.deiconify()
    imagen = ImageTk.PhotoImage(imagen)
    tk.Label(master=pantalla, image=imagen).pack()

    #Bloquea el flujo del código para que el imagen se pueda mostrar. El código sigue cuando
    #el usuario cerre la pantalla
    pantalla.mainloop()

    # Regenera la pantalla después de cerrar para que más simpledialogs y imagenes
    # se puedan mostrar
    pantalla = Tk()
    pantalla.withdraw()


def mugido():
    mostrar_imagen('vaca.jpg')
    playsound('mugido.wav')


def graznido():
    mostrar_imagen('pato.jpg')
    playsound('graznido.wav')


def guau():
    mostrar_imagen('perro.jpg')
    playsound('guau.wav')


def miau():
    mostrar_imagen('gato.jpg')
    playsound('miau.wav')


def grito_llama():
    mostrar_imagen('llama.jpg')
    playsound('llama.wav')


if __name__ == '__main__':
    animales()
