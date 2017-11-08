# encoding: UTF-8
# Autor: Aaron Villanueva

import pygame


ANCHO = 800
ALTO = 600

fondo=(0,0,0)
principal=(255,255,255)
def dibujar():
    menuPrincipal=True
    jugando=False
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
        
        ventana.fill(fondo)
        
        if menuPrincipal==True:
            pygame.draw.rect(ventana, principal, (30, 30, ANCHO-60, ALTO-60), 5)
            
            menuPrincipal=False
            jugando=True
        
        if jugando==True:
        

        # Dibujar, aquí haces todos los trazos que requieras
        pygame.draw.circle(ventana, principal, (ANCHO//2, ALTO//2), 200, 2)

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame


def main():
    dibujar()


main()
