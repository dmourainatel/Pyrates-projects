import pygame
import random
from pygame.locals import *

pygame.init()
 
display = pygame.display.set_mode((640,480))
carrinho = pygame.image.load("2.jpg")

font = pygame.font.Font(None,50)

inimigos = []
timer = 0
score = 0

class Inimigo:
    def __init__(self,sprite):
        self.x = random.randint(0,640)
        self.y = random.randint(0,480)
        self.sprite = sprite
        self.rect = Rect(self.x,self.y, sprite.get_width(), sprite.get_height())

    def draw(self,display):
        display.blit(self.sprite,(self.x,self.y))   
        
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
    	    pygame.exit()
        elif event.type == MOUSEBUTTONDOWN:
            for e in inimigos:
                if e.rect.collidepoint(mouse_pos):
                    inimigos.remove(e)
                    score += 10
                    break    

    display.fill((0,0,0))
    mouse_pos = pygame.mouse.get_pos()
    
    if timer % 1000 == 0:			
        inimigos.append(Inimigo(carrinho))

    for inimigo in inimigos:
        inimigo.draw(display)

    scoreText = font.render("Score: "+ str(score),True,(255,255,255))    
    display.blit(scoreText,(10,10))
    timer += 1        
    pygame.display.flip()
	

    
