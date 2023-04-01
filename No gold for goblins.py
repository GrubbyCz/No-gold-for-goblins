#základní blbosti
import sys
import random
import os
import pygame
from pygame.sprite import Sprite
from math import radians, sin, cos
pygame.init()


#proměnné
ZELENÁ = (17, 207, 40)
velikost_x = 200
velikost_y = 200
ROZLISENI_X = 1920
ROZLISENI_Y = 1022
FPS = 60
goblin_velikost_x = 75
goblin_velikost_y = 75

tank1 = pygame.image.load("tank.png")
tank1 = pygame.transform.scale(tank1, (velikost_x, velikost_y))
rychlost = 5
running = True
pozice_x = (ROZLISENI_X - velikost_x) / 2
pozice_y = (ROZLISENI_Y - velikost_y) / 2
font = pygame.font.SysFont('Consolas', 30)
horníx = random.randint(0, 1000)
horníy = ROZLISENI_X - (ROZLISENI_X + 70)
mince = 5
trezor = pygame.image.load("trezor.png")
broke = pygame.image.load("broke.png")

rychlostg0 = 1
rychlostg1 = 2
rychlostg2 = 3
rychlostg3 = 4
rychlostg4 = 2.5

#zobrazení okna
hodiny = pygame.time.Clock()
okno = pygame.display.set_mode((ROZLISENI_X, ROZLISENI_Y))
pygame.display.set_caption("No gold for goblins")

pozice = pygame.math.Vector2(okno.get_rect().center)
smer = pygame.math.Vector2(5, 0)
uhel = smer.angle_to((1, 0))


#GOBLIN a NILBOG

goblin0 = pygame.image.load("goblin.png")
goblin0 = pygame.transform.scale(goblin0, (goblin_velikost_x, goblin_velikost_y))
goblin1 = pygame.image.load("goblin.png")
goblin1 = pygame.transform.scale(goblin1, (goblin_velikost_x, goblin_velikost_y))
goblin2 = pygame.image.load("goblin.png")
goblin2 = pygame.transform.scale(goblin2, (goblin_velikost_x, goblin_velikost_y))
goblin3 = pygame.image.load("goblin.png")
goblin3 = pygame.transform.scale(goblin3, (goblin_velikost_x, goblin_velikost_y))
goblin4 = pygame.image.load("goblin.png")
goblin4 = pygame.transform.scale(goblin4, (goblin_velikost_x, goblin_velikost_y))

nilbog = pygame.image.load("nilbog.png")
nilbog = pygame.transform.scale(nilbog, (goblin_velikost_x, goblin_velikost_y))

#enemy x y
enemy0_x = random.randint(0, 1900)
enemy0_y = random.randint(1, 1)
enemy0_otoč = False 

enemy1_x = random.randint(0, 1900)
enemy1_y = random.randint(1, 1)
enemy1_otoč = False 

enemy2_x = random.randint(0, 1900)
enemy2_y = random.randint(1, 1)
enemy2_otoč = False

enemy3_x = random.randint(0, 1900)
enemy3_y = random.randint(1, 1)
enemy3_otoč = False

enemy4_x = random.randint(0, 1900)
enemy4_y = random.randint(1, 1)
enemy4_otoč = False

#nilbog x y
nilbog0_x = random.randint(0, 1900)
nilbog0_y = random.randint(1, 1)

nilbog1_x = random.randint(0, 1900)
nilbog1_y = random.randint(1, 1)

nilbog2_x = random.randint(0, 1900)
nilbog2_y = random.randint(1, 1)

nilbog3_x = random.randint(0, 1900)
nilbog3_y = random.randint(1, 1)


#enemy
def enemy0(x, y):
    okno.blit(goblin0, (x, y))

def enemy1(x, y):
    okno.blit(goblin1, (x, y))

def enemy2(x, y):
    okno.blit(goblin2, (x, y))

def enemy3(x, y):
    okno.blit(goblin3, (x, y))
    
def enemy4(x, y):
    okno.blit(goblin4, (x, y))

#nilbog    
def nilbog0(x, y):
    okno.blit(nilbog, (x, y))

def nilbog1(x, y):
    okno.blit(nilbog, (x, y))

def nilbog2(x, y):
    okno.blit(nilbog, (x, y))

def nilbog3(x, y):
    okno.blit(nilbog, (x, y))    


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
       
#okno
    okno.fill(ZELENÁ)


#pohyb dopředu a dozadu
    
    if klavesy[pygame.K_w]:
        pozice += smer
    if klavesy[pygame.K_s]:
        pozice -= smer
    if klavesy[pygame.K_a]:
        smer.rotate_ip(-2)
    if klavesy[pygame.K_d]: 
        smer.rotate_ip(2)      
       
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
    
    
 
     
    
    
    
 

    
#hitboxy

    hitbox_trezor = pygame.draw.rect(okno, ZELENÁ, (0, ROZLISENI_Y - 40, 1920, 40))
    hitbox_goblin0 = pygame.draw.rect(okno, ZELENÁ, (enemy0_x, enemy0_y, goblin_velikost_x, goblin_velikost_y))
    hitbox_goblin1 = pygame.draw.rect(okno, ZELENÁ, (enemy1_x, enemy1_y, goblin_velikost_x, goblin_velikost_y))
    hitbox_goblin2 = pygame.draw.rect(okno, ZELENÁ, (enemy2_x, enemy2_y, goblin_velikost_x, goblin_velikost_y))
    hitbox_goblin3 = pygame.draw.rect(okno, ZELENÁ, (enemy3_x, enemy3_y, goblin_velikost_x, goblin_velikost_y))
    hitbox_goblin4 = pygame.draw.rect(okno, ZELENÁ, (enemy4_x, enemy4_y, goblin_velikost_x, goblin_velikost_y))    
    kolize_0 = pygame.Rect.colliderect(hitbox_trezor, hitbox_goblin0)
    kolize_1 = pygame.Rect.colliderect(hitbox_trezor, hitbox_goblin1)
    kolize_2 = pygame.Rect.colliderect(hitbox_trezor, hitbox_goblin2)
    kolize_3 = pygame.Rect.colliderect(hitbox_trezor, hitbox_goblin3)
    kolize_4 = pygame.Rect.colliderect(hitbox_trezor, hitbox_goblin4)
    
    if kolize_0:
        mince -= 1
        enemy0_otoč = True
    if kolize_1:
        mince -= 1
        enemy1_otoč = True    
    if kolize_2:
        mince -= 1
        enemy2_otoč = True
    if kolize_3:
        mince -= 1
        enemy3_otoč = True
    if kolize_4:
        mince -= 1
        enemy4_otoč = True
    
    
    
#NEPŘÁTELÉ...    

#goblin...0
    
    if enemy0_y > 950:
        enemy0_otoč = True
        
    if enemy0_y < 20:
        enemy0_otoč = False 
 
    if enemy0_otoč == False:
        enemy0(enemy0_x, enemy0_y)
        enemy0_y += rychlostg0

        goblin0 = pygame.image.load("goblin.png")
        goblin0 = pygame.transform.scale(goblin0, (goblin_velikost_x, goblin_velikost_y))
        
    if enemy0_otoč == True:
        enemy0(enemy0_x, enemy0_y)
        enemy0_y -= rychlostg0

        goblin0 = pygame.image.load("nilbog.png")
        goblin0 = pygame.transform.scale(goblin0, (goblin_velikost_x, goblin_velikost_y))
        if enemy0_y <= 20:
            enemy0_x = random.randint(0, 1900)
     
            
#goblin...1    
    
    if counter >= 30:
        if enemy1_y > 950:
            enemy1_otoč = True
            
        if enemy1_y < 20:
            enemy1_otoč = False 
     
        if enemy1_otoč == False:
            enemy1(enemy1_x, enemy1_y)
            enemy1_y += rychlostg1

            goblin1 = pygame.image.load("goblin.png")
            goblin1 = pygame.transform.scale(goblin1, (goblin_velikost_x, goblin_velikost_y))
            
        if enemy1_otoč == True:
            enemy1(enemy1_x, enemy1_y)
            enemy1_y -= rychlostg1

            goblin1 = pygame.image.load("nilbog.png")
            goblin1 = pygame.transform.scale(goblin1, (goblin_velikost_x, goblin_velikost_y))
            if enemy1_y <= 20:
                enemy1_x = random.randint(0, 1900)
        
       
#goblin...2   
    
    if counter >= 60:
        if enemy2_y > 950:
            enemy2_otoč = True
            
        if enemy2_y < 20:
            enemy2_otoč = False 
     
        if enemy2_otoč == False:
            enemy2(enemy2_x, enemy2_y)
            enemy2_y += rychlostg2

            goblin2 = pygame.image.load("goblin.png")
            goblin2 = pygame.transform.scale(goblin2, (goblin_velikost_x, goblin_velikost_y))
            
        if enemy2_otoč == True:
            enemy2(enemy2_x, enemy2_y)
            enemy2_y -= rychlostg2

            goblin2 = pygame.image.load("nilbog.png")
            goblin2 = pygame.transform.scale(goblin2, (goblin_velikost_x, goblin_velikost_y))
            if enemy2_y <= 20:
                enemy2_x = random.randint(0, 1900)
        
        
#goblin...3    
    
    if counter >= 90:   
        if enemy3_y > 950:
            enemy3_otoč = True
            
        if enemy3_y < 20:
            enemy3_otoč = False 
     
        if enemy3_otoč == False:
            enemy3(enemy3_x, enemy3_y)
            enemy3_y += rychlostg3

            goblin3 = pygame.image.load("goblin.png")
            goblin3 = pygame.transform.scale(goblin3, (goblin_velikost_x, goblin_velikost_y))
            
        if enemy3_otoč == True:
            enemy3(enemy3_x, enemy3_y)
            enemy3_y -= rychlostg3

            goblin3 = pygame.image.load("nilbog.png")
            goblin3 = pygame.transform.scale(goblin3, (goblin_velikost_x, goblin_velikost_y))
            if enemy3_y <= 20:
                enemy3_x = random.randint(0, 1900)


#goblin...4    

    if counter >= 120:   
        if enemy4_y > 950:
            enemy4_otoč = True
            
        if enemy4_y < 20:
            enemy4_otoč = False 
     
        if enemy4_otoč == False:
            enemy4(enemy4_x, enemy4_y)
            enemy4_y += rychlostg4

            goblin4 = pygame.image.load("goblin.png")
            goblin4 = pygame.transform.scale(goblin4, (goblin_velikost_x, goblin_velikost_y))
            
        if enemy4_otoč == True:
            enemy4(enemy4_x, enemy4_y)
            enemy4_y -= rychlostg4

            goblin4 = pygame.image.load("nilbog.png")
            goblin4 = pygame.transform.scale(goblin4, (goblin_velikost_x, goblin_velikost_y))
            if enemy4_y <= 20:
                enemy4_x = random.randint(0, 1900)


#čas (zvýšení rychlosti pobíhání golinků)
    if counter == 10:
        rychlostg0 += 0.01
        rychlostg1 += 0.01
        rychlostg2 += 0.01
        rychlostg3 += 0.01
        rychlostg4 += 0.01
    if counter == 20:
        rychlostg0 += 0.01
        rychlostg1 += 0.01
        rychlostg2 += 0.01
        rychlostg3 += 0.01
        rychlostg4 += 0.01
    if counter == 70:
        rychlostg0 += 0.01
        rychlostg1 += 0.01
        rychlostg2 += 0.01
        rychlostg3 += 0.01
        rychlostg4 += 0.01


#konec     
    
    uhel = smer.angle_to((1, 0))
    tank = pygame.transform.rotate(tank1, uhel) 
    okno.blit(trezor, (0, ROZLISENI_Y - 40))
    text_mince = str(mince).rjust(3)   
    okno.blit(font.render(text_mince, True, (0, 0, 0)), (ROZLISENI_X / 2, ROZLISENI_Y - 40))
    okno.blit(tank, tank.get_rect(center = (round(pozice.x), round(pozice.y))))
    
    if mince <= 0:
        okno.blit(broke, (0, 0)) 
    
    okno.blit(font.render(text, True, (0, 0, 0)), (32, 48))   
    
#úplý konec
    pygame.display.update()
    hodiny.tick(FPS)