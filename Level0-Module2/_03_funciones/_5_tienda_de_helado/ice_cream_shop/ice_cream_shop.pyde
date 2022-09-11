# Cuándo este programa está completado, el programa va a dibujar un cono con tres
# trozos de helado, chispas, y una cereza a la cima


def setup():

    size(500,500)

    # Use la función crear_cono() para dibujar un cono para tu helado

    # Use la función crear_trozo() para añadir trozos de helado. Puede añadir
    # tantos trozos como quiere

    # Use la función crear_chispas() para añadir chispas a su helado

    # Escriba código a añadir una cereza a la cima de su helado
    # Pista: Elipsa



# ==================== DO NOT MODIFY THE CODE BELOW ============================

SCOOPSIZE = 150
scoops = 0
coneY = 320


def crear_cono():
     fill(188,126,49)
     triangle(190,320,310,300,255,500)


def crear_trozo(flavor):
     global scoops;
     noStroke()
     if flavor.lower() == "chocolate":
         fill(116,71,16)
     elif flavor.lower() == "strawberry":
         fill( 232 ,144,129)
     elif flavor.lower() == "vanilla":
         fill(245, 243, 227)
     else:
         print "ERROR: We don't have the flavor "+ flavor 
         return

     ellipse(width/2,coneY - 50 - (SCOOPSIZE*scoops)/2,SCOOPSIZE,SCOOPSIZE)
     scoops+=1


def crear_chispas(number_of_sprinkles):
    for i in range(number_of_sprinkles):
        fill(random(256),random(256),random(256))
        min_x = width/2-SCOOPSIZE/2 + 10
        max_x = SCOOPSIZE/3 +width/2 +10
        min_y = coneY-((SCOOPSIZE)*scoops)/2-40
        max_y = coneY
        sprinkle_area_x = random(min_x, max_x)
        sprinkle_area_y = random(min_y, max_y)
        sprinkle_width = random(2,9)
        sprinkle_height = random(2,9)
        ellipse(sprinkle_area_x,sprinkle_area_y,sprinkle_height,sprinkle_width)
