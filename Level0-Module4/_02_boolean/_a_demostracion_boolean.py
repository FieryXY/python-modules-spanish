"""
Demostración de Boolean
"""


# Boolean es una variable tipo que tiene dos valores:
#   True (Cierto)
#   False (Falso)
# Como int, double, y string variables, boolean variables pueden ser
# creadas escribiendo el nombre de la variable seguido de = True o = False
#   boolean_var = True
#   boolean_var = False
#
# Boolean variables o valores pueden ser utilizados directamente en if y elif statements:
#   boolean_var = True
#   if boolean_var:
#       print('boolean_var es Cierto!')
#
# Observe que "if boolean_var == True:" no es necesario.
#
# Booleanes son creados cuando hacemos comparaciones (<, > ==) entre variables o valores
#   boolean_var = 5 == 5            # True
#   es_Keith = nombre == 'Keith'      # True
#   es_fin_de_semana = dia == 'Sabado'  # False
#
# Boolean variables pueden ser toggled, es decir, alternados, usando el keyword 'not'
#   boolean_var = True
#   boolean_var2 = not boolean_var  # False

if __name__ == '__main__':
    # Dos variables de boolean
    boolean_var1 = True
    boolean_var2 = False

    # APUNTE - boolean_var1 == True no es necesario
    if boolean_var1:
        print('boolean_var1 es True!')
        if boolean_var2:
            print('boolean_var2 es True!')
        else:
            print('boolean_var2 es False!')
    else:
        print('boolean_var1 es False!')

    boolean_var3 = True
    for i in range(4):
        print('boolean_var3 es: ' + str(boolean_var3))
        boolean_var3 = not boolean_var3
