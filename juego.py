# encoding: UTF-8
# Autor: Aaron Villanueva

import pygame

def musica(pista):
    if pista==1:
        pygame.mixer.music.load("1.ogg")
    else:
        pygame.mixer.music.load("2.ogg")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)

anchoVentana = 800
altoVentana = 600

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
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
        
        ventana.fill(fondo)
        
        if evento.type==pygame.KEYDOWN:
            if evento.key==pygame.K_DOWN:
                seleccion+=20
                movimiento=True
            if evento.key==pygame.K_UP
                seleccion-=20
                movimiento=True
            if evento.key==pygame.K_LEFT:
                posicion-=20
                movimiento=True
            if evento.key==pygame.K_RIGHT:
                posicion+=20
                movimiento=True
            if evento.key==pygame.K_SPACE:
                disparar=True
            if evento.type==pygameKEYUP:
                movimiento=False
                disparar=False
                
        posicion, seleccion=pygame.mouse.get_pos()
        if posicion>=anchoVentana:
            posicion=anchoVentana
        elif posicion<=0:
            posicion=0
        if seleccion>= altoVentana-areaJuego:
           seleccion=altoVentana-areaJuego
        elif seleccion<=0:
           seleccion=0
                
                
        if menuPrincipal==True:
            ventana.fill(fondo)
            textoInicio = fuente.render("Empezar", 0, principal)
            posicionInicio = textoInicio.get_rect(center=(anchoVentana // 2, altoVentana // 2))
            ventana.blit(textoInicio, posicionInicio)
            if posicion==400:
                jugando=True
                menuPrincipal=False

        
        if jugando==True:
            pygame.draw.circle(ventana, principal, (anchoVentana//2, altoVentana//2), 200, 2)

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame


def main():
    dibujar()


main()
