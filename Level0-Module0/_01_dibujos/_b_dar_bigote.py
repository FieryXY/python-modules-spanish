import turtle
from PIL import Image

# ================= LAS INSTRUCCIONES SON AL PIE DE ESTE FICHERO ===================


def fijar_fondo(filename):
    try:
        image = Image.open(filename)
    except(FileNotFoundError, IOError):
        print("ERROR: No se puede buscar " + filename)
        return

    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(filename)


def anadir_bigote(filename):
    m = turtle.Turtle()

    m.hideturtle()
    window.addshape(filename)
    m.shape(filename)
    m.penup()
    m.speed(0)

    return m


# ====================== NO CAMBIE EL CÓDIGO ENCIMA ===========================

#Traducciones:
# Bigote - Moustache
# Mostrar Tortuga - Show Turtle
# Fijar el Fondo - Set Background


def pantalla_clic(x, y):
    print('Apretaste: x=' + str(x) + ', y=' + str(y))

    # 4. Muestre su bigote por llamar la función .showturtle()
    #bigote.showturtle()

    # 5. Mueva su bigote a una ubicación nueva con .goto(x,y)


if __name__ == '__main__':
    window = turtle.Screen()

    #1. Busque un imagen de una cara en línea en que quiere poner un bigote. 
    #Ponga el fichero en la carpeta con tu código

    # 2. Use la función fijar_fondo() para fijar el fondo. Ponga el nombre del fichero en el paréntesis
    fijar_fondo('emoji.png')

    # 3. Cree una variable que se llama "bigote" y hace que sea igual a anadir_bigote('bigote1.gif)
    # bigote = anadir_bigote('bigote.gif')


    # ===================== NO CAMBIE EL CÓDIGO DEBAJO ============================
    window.onclick(pantalla_clic)
    mi_tortuga.done()
