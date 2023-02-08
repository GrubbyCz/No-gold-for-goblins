import sys
import pygame

pygame.init()

ROZLISENI_X = 1920
ROZLISENI_Y = 1022
FPS = 60


hodiny = pygame.time.Clock()
okno = pygame.display.set_mode((ROZLISENI_X, ROZLISENI_Y))

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    klavesy = pygame.key.get_pressed()
    
    
    
pygame.display.update()
hodiny.tick(FPS)