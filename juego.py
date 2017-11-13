# encoding: UTF-8
# Autor: Roberto Martínez Román
# Muestra cómo utilizar pygame para escribir programas que dibujan en la pantalla

import pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)

def actualizarBalas(listaBalas,listaEnemigos):
    for bala in listaBalas:
        bala.rect.top-=5
    for e in listaEnemigos:
        e.rect.top+=5
    #Eliminar baas fuera de la pantalla
    for k in range (-1,-len(listaBalas)-1,-1):
        if listaBalas[k].rect.top<=-16:
            listaBalas.remove(listaBalas[k])
    for bala in listaBalas:
        borrarBala= False
        for enemigo in listaEnemigos:
            if bala.rect.colliderect(enemigo):
                listaEnemigos.remove(enemigo)
                borrarBala=True
        if borrarBala:
            listaBalas.remove(bala)


def dibujarMenu(ventana,btnJugar):
    ventana.blit(btnJugar.image, btnJugar.rect)

def dibujarJuego(ventana,btnJugar, lista,listaBalas,listaEnemigos):
    btnJugar.rect.left=100
    btnJugar.rect.top=100
    ventana.blit(btnJugar.image, btnJugar.rect)
    for enemigo in lista:
        ventana.blit(enemigo.image, enemigo.rect)
    for bala in listaBalas:
        ventana.blit(bala.image,bala.rect)
    actualizarBalas(listaBalas,listaEnemigos)

def generarEnemigos(listaEnemigos,imgBotonJugar):
    for x in range(3):
        for y in range(3):
            cx=50+x*260
            cy=100+y*100
            nuevo = pygame.sprite.Sprite()
            nuevo.image = imgBotonJugar
            nuevo.rect = imgBotonJugar.get_rect()
            nuevo.rect.left = cx
            nuevo.rect.top = cy
            listaEnemigos.append(nuevo)



def dibujar():
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    estado = "menu"  # jugando, termina
    imgBotonJugar =pygame.image.load("botonJugar.png")
    btnJugar=pygame.sprite.Sprite()
    btnJugar.image=imgBotonJugar
    btnJugar.rect=imgBotonJugar.get_rect(center=(400,400))
    imgBala=pygame.image.load("PEPE.png")

    listaEnemigos=[]
    generarEnemigos(listaEnemigos,imgBotonJugar)

    listaBalas=[]

    timer=0
    fps=30

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

            elif evento.type==pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if estado=="menu" :
                    xb,yb,anchoB,altoB=btnJugar.rect
                    if xm>xb and xm<=xb+anchoB:
                        estado="jugando"
                elif estado=="jugando":
                    nuevo=pygame.sprite.Sprite()
                    nuevo.image=imgBotonJugar
                    nuevo.rect=imgBotonJugar.get_rect()
                    nuevo.rect.left=xm
                    nuevo.rect.top=ym
                    listaEnemigos.append(nuevo)
            elif evento.type==pygame.KEYDOWN:
                if evento.key==pygame.K_SPACE:
                    bala=pygame.sprite.Sprite()
                    bala.image=imgBala
                    bala.rect=imgBala.get_rect()
                    bala.rect.left=ANCHO//2
                    bala.rect.top=ALTO-bala.rect.height
                    listaBalas.append(bala)



        # Borrar pantalla
        ventana.fill(BLANCO)
        timer+=1/fps

        # Dibujar, aquí haces todos los trazos que requieras
        if estado=="menu":
            dibujarMenu(ventana, btnJugar)
        elif estado=="jugando":
            dibujarJuego(ventana, btnJugar, listaEnemigos,listaBalas, listaEnemigos)

        pygame.draw.rect(ventana, VERDE_BANDERA, (30, 30, ANCHO-60, ALTO-60), 5)
        pygame.draw.circle(ventana, ROJO, (ANCHO//2, ALTO//2), 200, 2)


        pygame.display.flip()   # Actualiza trazos
        reloj.tick(fps)

    pygame.quit()   # termina pygame


def main():
    dibujar()


main()
