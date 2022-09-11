import random
from tkinter import Tk, Label, Button, messagebox
from tkinter import *
from PIL import ImageTk


def clic(args):
    #TODO 1) Ejecute el programa y juege algunas rondas de Piedra, Papel, o Tijeras.
    #   ¿La computadora siempre escoge la misma opción?

    # TODO 2) Cambie el valor de seleccion_oponente a ser igual de un número aleatorio entre 1 y 3
    seleccion_oponente = 1
    
    # TODO 3) Ejecute el programa otra vez. ¿El resultado es diferente?

    seleccion = 1

    if args == "PAPEL":
        seleccion = 2
    elif args == "TIJERAS":
        seleccion = 3

    messagebox.showinfo(None, "Ud. Escogió: " + args + ".\n"
                        + "La computadora escogió: " + opp_seleccionar(seleccion_oponente) + ".\n")

    if seleccion == seleccion_oponente:
        messagebox.showinfo(None, "Empate. Puede jugar otra vez")
    elif (seleccion == 1 and seleccion_oponente == 3) or (seleccion == 2 and seleccion_oponente == 1) or (
            seleccion == 3 and seleccion_oponente == 2):
        messagebox.showinfo(None, "Gana!")
    else:
        messagebox.showinfo(None, "Pierde :(")


def opp_seleccionar(s):
    if s == 1:
        return "PIEDRA"
    elif s == 2:
        return "PAPEL"
    elif s == 3:
        return "TIJERAS"


if __name__ == '__main__':
    pantalla = Tk()
    pantalla.title("Rock, Paper, Scissors") #Title = Título
    pantalla.geometry("1075x250")
    pantalla.configure(background="grey") #Background = Fondo, Grey = Gris

    Label(pantalla, text="Elija su Arma!", bg="grey").pack(side="left")
    #Label es como texto en la pantalla

    #file='piedra.png'

    img_piedra = ImageTk.PhotoImage(file='piedra.png') #Usado para crear un imagen en la pantalla
    img_papel = ImageTk.PhotoImage(file='papel.jpeg')
    img_tijeras = ImageTk.PhotoImage(file='tijeras.jpeg')
    Button(pantalla, image=img_piedra, command=lambda: clic("PIEDRA")).pack(side="left")
    Button(pantalla, image=img_papel, command=lambda: clic("PAPEL")).pack(side="left")
    Button(pantalla, image=img_tijeras, command=lambda: clic("TIJERAS")).pack(side="left")

    # Start the GUI
    pantalla.mainloop()
