#základní blbosti
import sys
import random
import os
import pygame
from pygame.sprite import Sprite
from math import radians, sin, cos
pygame.init()




#proměnné
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
running = True
pozice_x = (ROZLISENI_X - velikost_x) / 2
pozice_y = (ROZLISENI_Y - velikost_y) / 2
font = pygame.font.SysFont('Consolas', 30)
horníx = random.randint(0, 1000)
horníy = ROZLISENI_X - (ROZLISENI_X + 70)
dolníx = 4
dolníy = 4
praváx = 4
praváy = 4
leváx = 4
leváy = 4
enemyspeed = 2

#goblin
def enemy():
    goblin = pygame.image.load("goblin.png")

    goblin = pygame.transform.rotozoom(goblin, 180, 1)
    okno.blit(goblin, (300, 600))



#zobrazení okna
hodiny = pygame.time.Clock()
okno = pygame.display.set_mode((ROZLISENI_X, ROZLISENI_Y))
pygame.display.set_caption("No gold for goblins")

pozice = pygame.math.Vector2(okno.get_rect().center)
smer = pygame.math.Vector2(5, 0)
uhel = smer.angle_to((1, 0))



#timer
counter, text = 0, '0'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)


#střala


class Bullet(pygame.sprite.Sprite):
    def __init__(self, mouse, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([4, 10])
        self.image.fill(black)
        self.mouse_x, self.mouse_y = mouse[0], mouse[1]
        self.player = player
        self.rect = self.image.get_rect()
    def update(self):
        speed = 4.
        range = 200
        distance = [self.mouse_x - self.player[0], self.mouse_y - self.player[1]]
        norm = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
        direction = [distance[0] / norm, distance[1 ] / norm]
        bullet_vector = [direction[0] * speed, direction[1] * speed]
        self.rect.x -= bullet_vector[0]
        self.rect.y -= bullet_vector[1]

        bullet = Bullet(pygame.mouse.get_pos(), [player.rect.x, player.rect.y])




#konec
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
    
    if klavesy[pygame.K_w]:
        pozice += smer
    if klavesy[pygame.K_s]:
        pozice -= smer
    if klavesy[pygame.K_a]:
        smer.rotate_ip(-1)
    if klavesy[pygame.K_d]: 
        smer.rotate_ip(1)



     
    
        
   
     
     
     
#kontroly    
    if pozice.x > ROZLISENI_X:
        pozice.x = ROZLISENI_X
    if pozice.y > ROZLISENI_Y:
        pozice.y = ROZLISENI_Y
    if pozice.x < 0:
        pozice.x = 0
    if pozice.y < 0:
        pozice.y = 0
        
#střela
    
    
 
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     
    okno.fill(0)
    uhel = smer.angle_to((1, 0))
    
    tank = pygame.transform.rotate(tank1, uhel)
    
    enemy()
    okno.blit(pozadi, (0, 0))
    okno.blit(tank, tank.get_rect(center = (round(pozice.x), round(pozice.y))))
    okno.blit(font.render(text, True, (0, 0, 0)), (32, 48))   

#zbytečný řádek111111111111111111111111111111111111111111111111111111111111111111111111

    pygame.display.update()
    hodiny.tick(FPS)