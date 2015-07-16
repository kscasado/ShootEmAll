'''
This module is for helping keep track of the hit points and displaying the
players health

@author: Kevin


'''
import pygame
from media.SpriteSheet import SpriteSheet 
import game
class healthBar(pygame.sprite.Sprite):
    frames_Arr=[]
    def __init__(self):
        self.sheet = SpriteSheet("../media/healthBar.png",1,300,210)
        self.width=300
        self.height=52
        self.image = self.sheet.getImage(0,0,self.width,self.height,
                                         game.constants.WHITE)
       
         
    
    def update(self):
        if self.width>0:
            self.width-=30
            self.image = self.sheet.getImage(0,0,self.width,self.height,
                                             game.constants.WHITE)
    def draw(self,SCREEN):
        SCREEN.blit(self.image,(0,game.constants.HEIGHT-52))