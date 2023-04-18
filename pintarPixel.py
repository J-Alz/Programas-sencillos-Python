import cv2
from random import randint

def getBGR(pos:tuple,image):
    r = image.item(pos[1],pos[0],2)
    g = image.item(pos[1],pos[0],1)
    b = image.item(pos[1],pos[0],0)
    return f"Color:{r},{g},{b}"

def setBGR(pos:tuple,image,color:tuple):
    image.itemset((pos[1],pos[0],2),color[0])
    image.itemset((pos[1],pos[0],1),color[1])
    image.itemset((pos[1],pos[0],0),color[2])
    getBGR((pos[0],pos[1]),image)
    return image

def pixelRandom(lim_inf,lim_sup):
    x = randint(lim_inf,lim_sup)
    y = randint(lim_inf,lim_sup)
    print(f"Posición:x={x},y={y}")
    return x,y

def colorRandom():
    r = randint(0,254)
    g = randint(0,254)
    b = randint(0,254)
    return r,g,b

def generarPixel(image,i):
    for x in range(i):
        print(f"---PIXEL({x+1})---")
        #Escogemos un pixel al azar
        posicion = pixelRandom(0,99)
        #Tomamos el color de dicho pixel
        print(getBGR(posicion,image))
        #Lo cambiamos de color
        color = colorRandom()
        image = setBGR(posicion,image,color)

    return image

if __name__=='__main__':
    #Cargamos el lienzo
    image = cv2.imread('lienzo.png')#100x100

    image = generarPixel(image,100)

    cv2.imwrite('newImagen.png',image)
    #cv2.imshow('imagen',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    