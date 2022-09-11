import turtle
from PIL import Image

# ================= Instrucciones Están Al Pie de Este Fichero ===================


#Traducciones Nuevos
# Devolver o Dar: Return

def fijar_fondo(filename):
    try:
        image = Image.open(filename)
    except(FileNotFoundError, IOError):
        print("ERROR: Unable to find file " + filename)
        return

    window.setup(image.width + 100, image.height + 100, startx=0, starty=0)
    window.bgpic(filename)


class Ojo:
    def __init__(self, ojo=None, x=0, y=0, radio=30):
        self.eye = eye
        self.x = x
        self.y = y
        self.radius = radius
        
        self.eye.penup()
        
    def draw(self):
        self.eye.begin_fill()
        self.eye.goto(self.x, self.y)
        self.eye.circle(radius=self.radius, steps=20)
        self.eye.end_fill()

# ====================== NO CAMBIE EL CÓDIGO ENCIMA ===========================


def pantalla_clic(x, y):
    print('Hizo clic: x=' + str(x) + ', y=' + str(y))


def teclado_clic():
    print('Hizo clic en el espaciador')
    
    # RAYO LÁSER. Este código va a hacer que su elipse se mueva debajo y a la derecha cuando
    # Ud. hace clic en el espaciador. Ejecute el programa a probarlo

    # 10. Aumente "x" y "y" de los 2 ojos por 5:
    #   Ej. eye_izquierda += 5
    
    # 11. Call the .draw() method for both eye variables.
    # 11. Use la función draw() con ambas las variables de ojo
    #   (Draw = Dibujar)


if __name__ == '__main__':
    pantalla = turtle.Screen()
    
    #1. Busque un imagen de un gato con ojos GRANDES O use un de los dos imagenes proveídos.
    #   a. Busque un imagen con Google. El imagen necesita ser un fichero de .gif
    #   b. "Right Click" un imagen y seleccione "Save Image As"
    #   c. Cambie el nombre del imagen a algo corto (Ej. cat.gif)
    #   d. Guarde el imagen en su computadora
    #   e. Coloque el imagen en este fichero (_04_juegos_asombrosos)

    # 2. Use la función fijar_fondo() con el nombre de su imagen por dentro de los paréntesis
        # Ej. fijar_fondo("cat.gif")

    # 3. Cree una tortuga nueva que se llama "mi_tortuga"

    # 4. Fije el color de la tortuga y el pencolor a rojo (o cualquier color Ud. quiere)
    #   Puede usar .color('red', 'red').
    #   Rojo = Red

    # 5. Fije el ancho a 0 para que un perímetro no está dibujado

    # 6. Fije la velocidad de la tortuga a 0 (más rápido)

    # 7. Ejecute el programa y haga clic en un de los ojos del gato. La ubicación (x,y) del ojo
    #   va a estar imprimido al debajo de su pantalla Processing.
    
    # 8. Después de buscar (x,y) de los ojos, úselos a crear dos variables de Ojo:
        #ojo_izquierda = Ojo(ojo=mi_tortuga, x=-34, y=11, radio=30)
        #ojo_derecha = Ojo(ojo=mi_tortuga, x=40, y=-5, radio=30)

    # 9. Use la función .draw() en ambos los ojos
        #Ej. ojo_izquierda.draw()
        # Dibujar = Draw


# ===================== NO CAMBIE EL CÓDIGO DEBAJO ============================
    pantalla.onclick(pantalla_clic)
    pantalla.onkeypress(teclado_clic, 'space')
    pantalla.listen()
    mi_tortuga.done()
