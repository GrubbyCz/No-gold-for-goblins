import sys
import pygame

pygame.init()

velikostx = 150
velikosty = 200
ROZLISENI_X = 1920
ROZLISENI_Y = 1022
FPS = 60
pozadi = pygame.image.load("pozadi.png")
pozadi = pygame.transform.scale(pozadi, (ROZLISENI_X, ROZLISENI_Y))
tank = pygame.image.load("tank.png")
tank = pygame.transform.scale(tank, (velikostx, velikosty))


pozice_x = (ROZLISENI_X - velikostx) / 2
pozice_y = (ROZLISENI_Y - velikosty) / 2


#zobrazení okna

hodiny = pygame.time.Clock()
okno = pygame.display.set_mode((ROZLISENI_X, ROZLISENI_Y))
okno.blit(pozadi, (0, 0))
okno.blit(tank, (pozice_x, pozice_y)) 
pygame.display.set_caption("No gold for goblins")


while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    hodiny.tick(FPS)