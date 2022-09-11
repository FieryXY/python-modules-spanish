import random
import sys
from tkinter import messagebox, Tk
from playsound import playsound


def abrir_la_caja():
    pass

    # TODO: Su misión: Use la función usar_contrasena para abrir la caja fuerte
    #   por tratar todas las combinaciones posibles


# ======================= NO CAMBIE EL CÓDIGO DEBAJO =========================

wekncrzpasfdkjhcfjse = random.randint(0, 999)


def usar_contrasena(suposicion):
    print("Tratando " + str(suposicion))

    contrasena = 999999 - wekncrzpasfdkjhcfjse

    if suposicion == contrasena:
        messagebox.showinfo(None, "Felicitaciones! Abrió la caja fuerte con " + str(guess))
        sonar_el_sonido_del_exito()
        sys.exit(0)


def sonar_el_sonido_del_exito():
    playsound('me-gusta.wav')


if __name__ == '__main__':
    pantalla = Tk()
    pantalla.withdraw()
    abrir_la_caja()
