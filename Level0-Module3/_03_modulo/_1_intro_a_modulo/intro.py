import random

if __name__ == '__main__':

    # TODO:
    # Módulo en realidad significa "resto de la división".
    # Sin embargo, es más fácil de entender desde algunos ejemplos
    # -
    # Un uso común para el módulo es probar si un número es par o impar.
    # Para hacer esto, divida el número por 2.
    # Si el resto es cero, el número es par, pero si el resto es uno,
    # el número es impar.
    # En código esto sería así:

    for i in range(3):
        numero = random.randint(0, 100)
        if numero % 2 == 0:
            print(str(numero) + " es par")
        else:
            print(str(numero) + " es impar")

    # TODO: Un otro uso para el módulo es rastrear cada 20 veces que un bucle se ejecuta, como se muestra a continuación:
    for i in range(101):
        if i % 20 == 0:
            print("i es: " + str(i) + ", 20 repiticiones completadas")
