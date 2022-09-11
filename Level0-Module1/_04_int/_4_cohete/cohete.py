from tkinter import *

ancho_pantalla = 800
ancho_altura = 800
root = Tk()

cuadro = Canvas(root, width=ancho_pantalla, height=ancho_altura, borderwidth=0, highlightthickness=0, bg="#000050")
cuadro.grid()


# This code runs whenever the mouse is clicked on the window
def raton_clic(evento):
    # Dibuje un fondo de azul oscuro
    cuadro.create_rectangle(0, 0, ancho_pantalla, ancho_altura, fill="#000050")

    # "x" y "y" son iguales a la ubicación del cursor en la pantalla
    x = evento.x
    y = evento.y

    #Estos son las ubicaciones de tres puntos de un triángulo ("x" y "y")
    puntos = [x, y, x - 50, y + 100, x + 50, y + 100]
    cuadro.create_polygon(points, fill='gray', width=2) # draws triangle

    # 1. Añada detalles a su cohete para se vea mejor. Puede mirar "cohete.png" como inspiración
    
    # 2. Modifique las ubicaciones de la forma encima para que el cohete esté dibujado
    #   a la ubicación del clic del cursor
    

# ====================== NO CAMBIE EL CÓDIGO DEBAJO ========================

canvas.bind("<Button-1>", raton_clic)

root.mainloop()
