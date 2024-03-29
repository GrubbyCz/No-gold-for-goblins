#základní blbosti
import sys
import random
import os
import pygame
from pygame.sprite import Sprite
from math import radians, sin, cos
pygame.init()
pygame.mixer.init()

#proměnné

ZELENÁ = (17, 207, 40)
velikost_x = 200
velikost_y = 200
ROZLISENI_X = 1920
ROZLISENI_Y = 1022
FPS = 60
goblin_velikost_x = 75
goblin_velikost_y = 75
goblinM_velikost_x = 125
goblinM_velikost_y = 125

tank1 = pygame.image.load("tank.png")
tank1 = pygame.transform.scale(tank1, (velikost_x, velikost_y))
rychlost = 5
running = True
pozice_x = (ROZLISENI_X - velikost_x) / 2
pozice_y = (ROZLISENI_Y - velikost_y) / 2
font = pygame.font.SysFont('Consolas', 30)
horníx = random.randint(0, 1000)
horníy = ROZLISENI_X - (ROZLISENI_X + 70)
mince = 100
trezor = pygame.image.load("trezor.png")
broke = pygame.image.load("broke.png")
pif = pygame.mixer.Sound("pif.mp3")
zivotM = 3

rychlostg0 = 1
rychlostg1 = 2
rychlostg2 = 3
rychlostg3 = 4
rychlostg4 = 2.5
rychlostgM = 3


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
goblinM = pygame.image.load("goblin3.png")
goblinM = pygame.transform.scale(goblinM, (goblinM_velikost_x, goblinM_velikost_y))

nilbog = pygame.image.load("nilbog.png")
nilbog = pygame.transform.scale(nilbog, (goblin_velikost_x, goblin_velikost_y))
nilbogM = pygame.image.load("nilbog3.png")
nilbogM = pygame.transform.scale(nilbogM, (goblinM_velikost_x, goblinM_velikost_y))

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

enemyM_x = random.randint(0, 1900)
enemyM_y = random.randint(1, 1)
enemyM_otoč = False


#nilbog x y

nilbog0_x = random.randint(0, 1900)
nilbog0_y = random.randint(1, 1)

nilbog1_x = random.randint(0, 1900)
nilbog1_y = random.randint(1, 1)

nilbog2_x = random.randint(0, 1900)
nilbog2_y = random.randint(1, 1)

nilbog3_x = random.randint(0, 1900)
nilbog3_y = random.randint(1, 1)

nilbog4_x = random.randint(0, 1900)
nilbog4_y = random.randint(1, 1)

nilbogM_x = random.randint(0, 1900)
nilbogM_y = random.randint(1, 1)


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

def enemyM(x, y):
    okno.blit(goblinM, (x, y))


#nilbog    

def nilbog0(x, y):
    okno.blit(nilbog0, (x, y))

def nilbog1(x, y):
    okno.blit(nilbog1, (x, y))

def nilbog2(x, y):
    okno.blit(nilbog2, (x, y))

def nilbog3(x, y):
    okno.blit(nilbog3, (x, y))    

def nilbog4(x, y):
    okno.blit(nilbog4, (x, y))

def nilbogM(x, y):
    okno.blit(nilbogM, (x, y))
    
    
#timer

counter, text = 0, '0'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)


#střala
    
class Bullet(Sprite):
    def __init__(self, position, direction):
        super().__init__()
        self.image = pygame.image.load("bobek.png") 
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=position)
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        self.direction = direction
        self.speed = 10

    def update(self):
        self.rect.move_ip(self.speed * self.direction[0], self.speed * self.direction[1])
        self.hitbox.move_ip(self.speed * self.direction[0], self.speed * self.direction[1])
        if not okno.get_rect().colliderect(self.rect):
            self.kill()

bullets = pygame.sprite.Group()


#konec

while True:
    klavesy = pygame.key.get_pressed()
    for udalost in pygame.event.get():
        if udalost.type == pygame.USEREVENT:
            if mince > 0:
                counter += 1     
                text = str(counter).rjust(3) 
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            run = False
        elif udalost.type == pygame.KEYDOWN:
            if udalost.key == pygame.K_SPACE:
                bullet = Bullet(pozice, smer)
                bullets.add(bullet)
                pif.play()


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
        
    
#hitboxy

    hitbox_trezor = pygame.draw.rect(okno, ZELENÁ, (0, ROZLISENI_Y - 40, 1920, 40))
    hitbox_goblin0 = pygame.draw.rect(okno, ZELENÁ, (enemy0_x, enemy0_y, goblin_velikost_x, goblin_velikost_y))
    hitbox_goblin1 = pygame.draw.rect(okno, ZELENÁ, (enemy1_x, enemy1_y, goblin_velikost_x, goblin_velikost_y))
    hitbox_goblin2 = pygame.draw.rect(okno, ZELENÁ, (enemy2_x, enemy2_y, goblin_velikost_x, goblin_velikost_y))
    hitbox_goblin3 = pygame.draw.rect(okno, ZELENÁ, (enemy3_x, enemy3_y, goblin_velikost_x, goblin_velikost_y))
    hitbox_goblin4 = pygame.draw.rect(okno, ZELENÁ, (enemy4_x, enemy4_y, goblin_velikost_x, goblin_velikost_y))    
    hitbox_goblinM = pygame.draw.rect(okno, ZELENÁ, (enemyM_x, enemyM_y, goblinM_velikost_x, goblinM_velikost_y))
    
    kolize_0 = pygame.Rect.colliderect(hitbox_trezor, hitbox_goblin0)
    kolize_1 = pygame.Rect.colliderect(hitbox_trezor, hitbox_goblin1)
    kolize_2 = pygame.Rect.colliderect(hitbox_trezor, hitbox_goblin2)
    kolize_3 = pygame.Rect.colliderect(hitbox_trezor, hitbox_goblin3)
    kolize_4 = pygame.Rect.colliderect(hitbox_trezor, hitbox_goblin4)
    kolize_M = pygame.Rect.colliderect(hitbox_trezor, hitbox_goblinM)


#kolize...-mince    
    
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
    if kolize_M:
        mince -= 3
        enemyM_otoč = True 
    

#střela...zmizí
        
    for bullet in bullets:
        if bullet.hitbox.colliderect(hitbox_goblin0):
            bullet.kill()
            enemy0_x = random.randint(0, 1900)
            enemy0_y = random.randint(1, 1)
            if enemy0_otoč == True:   
                mince += 1
    
    
    for bullet in bullets:
        if bullet.hitbox.colliderect(hitbox_goblin1):
            bullet.kill()
            enemy1_x = random.randint(0, 1900)
            enemy1_y = random.randint(1, 1)
            if enemy1_otoč == True:   
                mince += 1
    
    
    for bullet in bullets:
        if bullet.hitbox.colliderect(hitbox_goblin2):
            bullet.kill()
            enemy2_x = random.randint(0, 1900)
            enemy2_y = random.randint(1, 1)
            if enemy2_otoč == True:   
                mince += 1
        
    
    for bullet in bullets:
        if bullet.hitbox.colliderect(hitbox_goblin3):
            bullet.kill()
            enemy3_x = random.randint(0, 1900)
            enemy3_y = random.randint(1, 1)
            if enemy3_otoč == True:   
                mince += 1
    
    
    for bullet in bullets:
        if bullet.hitbox.colliderect(hitbox_goblin4):
            bullet.kill()
            enemy4_x = random.randint(0, 1900)
            enemy4_y = random.randint(1, 1)
            if enemy4_otoč == True:   
                mince += 1
    
    
    for bullet in bullets:
        if bullet.hitbox.colliderect(hitbox_goblinM):
            bullet.kill()
            zivotM -= 1
    if zivotM == 0:
        zivotM = 3
        enemyM_x = random.randint(0, 1900)
        enemyM_y = random.randint(1, 1)
        if enemyM_otoč == True:   
             mince += 3
                
#sound
                  
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


#goblin...Miniboss
    
    if counter >= 150:   
        if enemyM_y > 950:
            enemyM_otoč = True
            
        if enemyM_y < 20:
            enemyM_otoč = False 
     
        if enemyM_otoč == False:
            enemyM(enemyM_x, enemyM_y)
            enemyM_y += rychlostgM

            goblinM = pygame.image.load("goblin3.png")
            goblinM = pygame.transform.scale(goblinM, (goblinM_velikost_x, goblinM_velikost_y))
            
        if enemyM_otoč == True:
            enemyM(enemyM_x, enemyM_y)
            enemyM_y -= rychlostgM

            goblinM = pygame.image.load("nilbog3.png")
            goblinM = pygame.transform.scale(goblinM, (goblinM_velikost_x, goblinM_velikost_y))
            if enemyM_y <= 20:
                enemyM_x = random.randint(0, 1900)


#čas (zvýšení rychlosti pobíhání golinků)
    
    if counter == 10:
        rychlostg0 += 0.01
        rychlostg1 += 0.01
        rychlostg2 += 0.01
        rychlostg3 += 0.01
        rychlostg4 += 0.01
        rychlostgM += 0.01
    if counter == 20:
        rychlostg0 += 0.01
        rychlostg1 += 0.01
        rychlostg2 += 0.01
        rychlostg3 += 0.01
        rychlostg4 += 0.01
        rychlostgM += 0.01
    if counter == 70:
        rychlostg0 += 0.01
        rychlostg1 += 0.01
        rychlostg2 += 0.01
        rychlostg3 += 0.01
        rychlostg4 += 0.01
        rychlostgM += 0.01
    if counter == 200:
        rychlostg0 += 0.1
        rychlostg1 += 0.1
        rychlostg2 += 0.1
        rychlostg3 += 0.1
        rychlostg4 += 0.1
        rychlostgM += 0.1
    if counter == 250:
        rychlostg0 += 0.1
        rychlostg1 += 0.1
        rychlostg2 += 0.1
        rychlostg3 += 0.1
        rychlostg4 += 0.1
        rychlostgM += 0.1
        
              
#konec     
    
    uhel = smer.angle_to((1, 0))
    tank = pygame.transform.rotate(tank1, uhel) 
    okno.blit(trezor, (0, ROZLISENI_Y - 40))
    text_mince = str(mince).rjust(3)   
    okno.blit(font.render(text_mince, True, (0, 0, 0)), (ROZLISENI_X / 2, ROZLISENI_Y - 40))
    okno.blit(tank, tank.get_rect(center = (round(pozice.x), round(pozice.y))))
    bullets.update()
    bullets.draw(okno)
    if mince <= 0:
        okno.blit(broke, (0, 0)) 
    
    okno.blit(font.render(text, True, (0, 0, 0)), (32, 48))   


#úplý konec
    pygame.display.update()
    hodiny.tick(FPS)