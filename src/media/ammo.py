'''
This module is for keeping track of how many bullets the user has

@author: Kevin
'''
import pygame
from media.SpriteSheet import SpriteSheet
import game

class ammo():
        
    def __init__(self):
        self.sheet = SpriteSheet("../media/ammoSheet.png",1,32,320) 
        self.bullets = 10
        self.image = self.sheet.getImage(0,0,32,320,game.constants.WHITE)
        
    def reload(self):
        self.bullets = 10
        #change back to full image
        self.image = self.sheet.getImage(0,0,32,320,game.constants.WHITE)
    def shoot(self):
        if self.bullets!=0:
            self.bullets-=1
        # change size of image to show 1 less bullet
        if self.bullets!=0:
            self.image=self.sheet.getImage(0,((10-self.bullets)*32),32,(
                                        self.bullets*32),game.constants.WHITE)
        else:
            self.image=self.sheet.getImage(0,0,0,(
                                        self.bullets*0),game.constants.WHITE)
    def draw(self,SCREEN):
        # 420 because image height is 320 and health bar can be up to 100
        
        SCREEN.blit(self.image,(0,game.constants.HEIGHT-372))