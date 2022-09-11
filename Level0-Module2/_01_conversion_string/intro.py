from tkinter import messagebox, Tk

#Traducciones Nuevos
#Se Necesita Hacer: To Do (TODO)
#Nada: None

if __name__ == '__main__':
    pantalla = Tk()
    pantalla.withdraw()

    # TODO: Ejecute el programa y observe la diferencia entre los dos casillas de mensaje
    #   La seguna casilla no suma los números
    #   str() cambia un número a texto
    #   "3"+"7"= "37"
    #    3 + 7 = 10
    num1 = 3
    num2 = 7
    messagebox.showinfo(None, num1 + num2)
    messagebox.showinfo(None, str(num1) + str(num2))

    # TODO: Puede convertir texto a un número con la función int()
    # La primera casilla de mensaje combina los 2 strings "3" y "7" para crear "37"
    # Después de convertir los textos a números, el + hace la adición regular de números
    num1_str = '3'
    num2_str = '7'
    messagebox.showinfo(None, num1_str + num2_str)
    messagebox.showinfo(None, int(num1_str) + int(num2_str))

    # TODO: Quite los "#" y ejecute el programa otra vez. Use str()
    # para imprimir num1 y num2
    # messagebox.showinfo(None, "num1 = " + num1 + " num2 = " + num2)