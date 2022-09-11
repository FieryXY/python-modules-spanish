import random
import turtle

#Traducciones
# Verde - Green
# Azul - Blue
# Forma - Shape
# Color de Perímetro - Pen Color
# Ancho - Width (wid)
# Largo - Length (len)
# Imprimir - Print

# Da un color aleatorio!
def dar_color_aleatorio():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

# ====================== NO CAMBIE EL CÓDIGO ENCIMA ===========================


def pantalla_clic(x, y):
    print('Aprestaste: x=' + str(x) + ', y=' + str(y))
    
    # 6. Use la función .penup() con mi_tortuga

    # 7. Mueva mi_tortuga a una ubicación nueva con .goto(x,y)


def tortuga_clic(x, y):
    print('turtle clic!')
    
    # 8. Crea un "for loop" a ejecutar pasos 9 y 10 tres veces
        
        # 9. Haga que la tortuga doble 360 grados con la función .right()
        
        # 10. Use la función .color() y dar_color_aleatorio() a cambiar el color
        #de su tortuga,
        # mi_tortuga.color(dar_color_aleatorio())


if __name__ == '__main__':
    window = turtle.Screen()
    window.setup(width=0.75, height=0.8, startx=0, starty=0)
    
    # 1. Cree una tortuga nueva que se llama "mi_tortuga"
    
    # 2. Haga la forma de su tortuga 'turtle', .shape('turtle')
    
    # 3. Fije el color de su tortuga con .color('green') y .pencolor('blue')
    
    #4. Fije el un ancho, largo, y el grueso del perímetro de nuestra tortuga
        #mi_tortuga.turtlesize(stretch_wid=10, stretch_len=10, outline=4)
            #stretch_wid es el Ancho, stretch_len es el Largo, y outline es el grueso del perímetro

    # 5. Quite el "#" de la siguente línea
    # mi_tortuga.onclick(tortuga_clic)

# ===================== DO NOT EDIT THE CODE BELOW ============================
    window.onclick(pantalla_clic)
    mi_tortuga.done()
