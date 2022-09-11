from tkinter import simpledialog, Tk
from playsound import playsound

puede_reproducir_sonidos = False


def reproducir_mister_zee():
    if puede_reproducir_sonidos:
        playsound('objetos_brillantes.wav')
    else:
        print("Mister Zee necesita objetos brillantes")


def muchos_objetos_brillantes():

    # TODO 1) Use la función arriba para reproducir Mister Zee

    # TODO 2) Pregunte al usuario cuantos objetos brillantes quiere
    
    # TODO 3) Reproduzca el sonido tantas veces como el usuario quiera

    pass


if __name__ == '__main__':
    pantalla = Tk()
    pantalla.withdraw()
    muchos_objetos_brillantes()
