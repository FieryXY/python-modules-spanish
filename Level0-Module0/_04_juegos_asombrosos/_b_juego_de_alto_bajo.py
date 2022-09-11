from tkinter import messagebox, simpledialog, Tk
import sys
import random

if __name__ == '__main__':
    pantalla = Tk()
    pantalla.withdraw()

    # 1. Cambie esta línea a dar un número aleatorio entre 1 y 100
    numero_aleatorio = random.randint(1, 10)

    # 2. Imprima la variable aleatoria del paso #1

    # 3. Cree un "for loop" para ejecutar pasos 4-10 diez veces

        # 4. Pídale al usuario una suposición en una casilla de mensaje sobre el valor de la variable
        #de paso #1

        # 5. Si la suposición es correcta
            # 6. Victoria. Use 'sys.exit(0)' para terminar el programa

        # 7. Si la suposición es demasiada alta
            # 8. Dígale que la suposición es demasiada alta

        # 9. Si la suposición es demasiada baja
            # 10. Dígale que la suposición es demasiada baja


    # 11. Afuera del bucle, dígale al usuario que perdió

    pantalla.mainloop()
