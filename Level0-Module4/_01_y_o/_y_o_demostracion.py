"""
Operaciones Lógicas 'and' y 'or'
"""

from tkinter import messagebox, simpledialog, Tk

# Las palabras claves de Python 'and' y 'or' se utilizan para comprobar si
# varias condiciones booleanas son verdaderas o falsas. 'And' significa 'y'. 'Or' significa 'o'. 
# Por ejemplo:
#   if nombre == 'Sally' or nombre == 'Sue':
#       print('Se llama Sally o Sue!')
# El 'or' chequea si cualquiera de las dos condiciones (nombre == 'Sally' o nombre == 'Sue') es verdadera.
# Si alguna condición es verdadera, la expresión es verdadera.
#
# El 'and' chequea que ambas condiciones sean verdaderas para que la expresión sea verdadera.
# Por ejemplo:
#   if edad > 12 and altura_en_pulgadas > 48:
#       print('Puedes subir el carruaje de la aceleración!')
# El print function solo se llamará si la edad es mayor que 12 y la altura_en_pulgadas es mayor que 48.
# Si ninguna condición es verdadera, el print function no se llamará.

if __name__ == '__main__':
    pantalla = Tk()
    pantalla.withdraw()

    nombre = simpledialog.askstring(None, "¿Cual es su nombre?")

    if nombre == 'Sally' or nombre == 'Sue':
        messagebox.showinfo(None, 'Se llama Sally o Sue!')
    else:
        messagebox.showwarning(None, 'No se llama Sally o Sue!')

    edad = simpledialog.askinteger(None, "¿Cuantos años tiene?")
    altura_pulgadas = simpledialog.askinteger(None, "¿Cuánto mide en pulgadas?")

    if edad > 12 and altura_pulgadas > 48:
        messagebox.showinfo(None, 'Puedes subir el carruaje de la aceleración!')
    else:
        messagebox.showerror(None, 'No tiene la altura y la edad suficiente para subir el carruaje de la aceleración')
