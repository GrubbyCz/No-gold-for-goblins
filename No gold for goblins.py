import sys
import pygame
from math import sin, cos

pygame.init()

velikost_x = 200
velikost_y = 200
ROZLISENI_X = 1920
ROZLISENI_Y = 1022
FPS = 60
pozadi = pygame.image.load("pozadi.png")
pozadi = pygame.transform.scale(pozadi, (ROZLISENI_X, ROZLISENI_Y))
tank1 = pygame.image.load("tank.png")
tank1 = pygame.transform.scale(tank1, (velikost_x, velikost_y))
rychlost = 5
uhel = 0
smer = 0
pozice_x = (ROZLISENI_X - velikost_x) / 2
pozice_y = (ROZLISENI_Y - velikost_y) / 2
font = pygame.font.SysFont('Consolas', 30)

#zobrazení okna

hodiny = pygame.time.Clock()
okno = pygame.display.set_mode((ROZLISENI_X, ROZLISENI_Y))
pygame.display.set_caption("No gold for goblins")

counter, text = 0, '0'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)


while True:
    klavesy = pygame.key.get_pressed()
    for udalost in pygame.event.get():
        if udalost.type == pygame.USEREVENT:
            counter += 1
            text = str(counter).rjust(3) 
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            run = False
            
#pohyb dopředu a dozadu
    if klavesy[pygame.K_DOWN]:
        pozice_y += rychlost
    if klavesy[pygame.K_UP]:
        pozice_y -= rychlost
#otočení doleva a doprava        
    if klavesy[pygame.K_LEFT]:
        uhel += 1
    if klavesy[pygame.K_RIGHT]:
        uhel -= 1
        
   
     
     
     
     
    if pozice_x > ROZLISENI_X - velikost_x:
        pozice_x = ROZLISENI_X - velikost_x
    if pozice_y > ROZLISENI_Y - velikost_y:
        pozice_y = ROZLISENI_Y - velikost_y
    if pozice_x < 0:
        pozice_x = 0
    if pozice_y < 0:
        pozice_y = 0
        
       
    tank = pygame.transform.rotate(tank1, uhel)
    okno.blit(pozadi, (0, 0))
    okno.blit(tank, (pozice_x, pozice_y))
    okno.blit(font.render(text, True, (0, 0, 0)), (32, 48))   

    pygame.display.update()
    hodiny.tick(FPS)