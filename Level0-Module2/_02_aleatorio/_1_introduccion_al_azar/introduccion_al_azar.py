import random

if __name__ == '__main__':

    # Prints out 5 random whole numbers between 0 and 100 (0 and 100 both included)

    # NÚMEROS ENTEROS ALEATORIOS
    #   random.randint(principio, terminacion)
    #   Random = Aleatorio
    #   Esta función genera un número entre el número en principio y el número en terminación (ambos números incluidos)

    #Imprime 5 números aleatorios enteros entre 0 y 100

    for i in range(5):
        numero = random.randint(0, 100)
        print(numero)

    # TODO Imprima 5 números aleatorios entre -50 y 5
    for i in range(5):

        pass

    #NÚMEROS DECIMALES ALEATORIOS
    #   random.uniform(principio, terminacion)
    #   uniform = uniforme
    #   principio: Mínimo
    #   terminacion: Máximo

    #Imprime 5 números decimales aleatorios entre 1.2 y 34.5 (ambos 1.2 y 34.5 incluidos)
    for i in range(5):
        numero = random.uniform(1.2, 34.5)
        print(numero)
        
    # TODO Imprima 5 números decimales aleatorios entre -123.45 and 67.89
    for i in range(5):

        pass
