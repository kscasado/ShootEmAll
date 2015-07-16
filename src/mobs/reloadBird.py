'''

This module is the bird that spawns from either side of the map and if 
it is hit then the user gets to reload
@author: Kevin
'''
import pygame
import game
from mobs.mob import Mob
from media.SpriteSheet import SpriteSheet
import random

class reloadBird(Mob):
    #setup the frames
    framesL_Arr=[]
    framesR_Arr=[]
    framesC_Arr=[]
    def __init__(self):
        self.isDead=False
        self.width=64
        self.height=64
        self.frames=3
        self.index=0
        self.vy=-3*(game.constants.HEIGHT/600)
        self.y = game.constants.HEIGHT/2
        self.sheet=SpriteSheet('../media/reloadBird1.png',3,192,256)
        self.timer=0
        self.name='reload'
        for j in range(0,4):
            image=self.sheet.getImage(64,j*64,64,64,game.constants.WHITE)
            self.framesL_Arr.append(image)
                ##flip the image
            pygame.transform.flip(image,True,False)
            self.framesR_Arr.append(image)
       
        
        
        i = random.randint(0,1)
        if i==1:
            self.vx=2*(game.constants.WIDTH/800)
            self.x=0
            self.framesC_Arr=self.framesR_Arr
        else:
            self.vx=-2*(game.constants.WIDTH/800)
            self.x=game.constants.WIDTH+self.width
            self.framesC_Arr=self.framesL_Arr
    def update(self):
        
        if self.timer%5==0:
            
            if self.index==self.frames-1:
                self.index=0
            else:
                    self.index+=1
        self.timer+=1
        self.x+=self.vx
        self.y+=self.vy
        self.vy+=.06
    def draw(self,SURFACE):
        SURFACE.blit(self.framesC_Arr[self.index],(self.x,self.y))