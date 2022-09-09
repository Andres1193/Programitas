import pygame, sys
from pygame.locals import *

# Iniciamos pygame
pygame.init()

# Creamos una ventana, pasamos los valores de nuestra ventana mediante una tupla (ancho, alto)
ventana = pygame.display.set_mode((400,300))

# Agregamos un título a nuestra ventana
pygame.display.set_caption("Titulo de la ventana")

# Agregamos un color al fondo de nuestra ventana RGV
colorFondo = (1, 150, 70)


while True:     # Creamos el bucle principal 
    ventana.fill(colorFondo)    # Añadimos el color a nuestra ventana
    for evento in pygame.event.get():   # Creamos un bucle que se encargara de comprobar los eventos que están ocurriendo
        if evento.type == QUIT: # Comprobamos el evento de SALIR
            pygame.quit() # Detenemos los modulos
            sys.exit() # Cerramos la ventana
        pygame.display.update() # Actualizamos la ventana    