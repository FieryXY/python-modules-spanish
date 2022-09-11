import random
from tkinter import messagebox, Tk

if __name__ == '__main__':
    pantalla = Tk()
    pantalla.withdraw()

    numero_aleatorio = random.randint(1, 5)

    print(numero_aleatorio)

    # TODO 1) Use cada valor de numero_aleatorio para dar el usuario un cumplido aleatorio

    # TODO 2) Repita todo el código encima 10 veces
