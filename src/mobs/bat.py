'''
Most Common mob that gets created, Just a regular bat that flys left and right
It does not have any attack abilities

@author: Kevin
'''
import pygame
from media.SpriteSheet import SpriteSheet
import game.constants
from mobs.mob import Mob  

class Bat(Mob):
    framesR_Arr =[]
    framesL_Arr = []
    framesCurr_Arr=[]
    def __init__(self,x,y,vx,vy):
        self.name='bat'
        self.frames = 4
        self.sheet = SpriteSheet('../media/batsprite.png',20,256,320)
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.index=0
        image = self.sheet.getImage(0,128,60,60,game.constants.BLACK)
        self.framesR_Arr.append(image)
        image = self.sheet.getImage(64,128,60,60,game.constants.BLACK)
        self.framesR_Arr.append(image)
        image = self.sheet.getImage(128,128,60,60,game.constants.BLACK)
        self.framesR_Arr.append(image)
        image = self.sheet.getImage(192,128,60,60,game.constants.BLACK)
        self.framesR_Arr.append(image)
        image = self.sheet.getImage(0,192.0,60,60,game.constants.BLACK)
        self.framesL_Arr.append(image)
        image = self.sheet.getImage(64,192 ,60,60,game.constants.BLACK)
        self.framesL_Arr.append(image)
        image = self.sheet.getImage(128,192,60,60,game.constants.BLACK)
        self.framesL_Arr.append(image)
        image = self.sheet.getImage(192,192,60,60,game.constants.BLACK)
        self.framesL_Arr.append(image)
        self.timer=0
        self.passes = 0   
        self.width=60
        self.height =60
        self.framesCurr_Arr=self.framesR_Arr
        
    def update(self):
        if self.vx<0:
            if self.framesCurr_Arr!=self.framesL_Arr:
                self.framesCurr_Arr=self.framesL_Arr
                self.index=0
        else:
            if self.framesCurr_Arr!=self.framesR_Arr:
                self.framesCurr_Arr=self.framesR_Arr
                self.index=0
        if self.timer%10==0:
            
            if self.index==self.frames-1:
                self.index=0
            else:
                    self.index+=1
        self.timer+=1
        self.x+=self.vx
        self.y+=self.vy
        self.checkWall()
    def checkWall(self):
        if(self.x+self.width>game.constants.WIDTH):
            self.vx=-self.vx
            self.framesCurr_Arr=self.framesL_Arr
            self.index=0
            self.update()
        if self.x<0:
            self.framesCurr_Arr=self.framesR_Arr
            self.index=0
            self.vx=-self.vx
            self.update()
        if self.y==(game.constants.HEIGHT-self.height):
            self.vy=0
            
    def isDead(self):
        self.vy=9
        self.vx=0
        self.isDead=True
    def collide(self,pos):
        if self.x<pos[0] and self.x+self.width>pos[0] :
            
            if self.y<pos[1] and self.y+self.height>pos[1]:
               
                return True
        
        return False
    
            
                  
    def draw(self,SURFACE):
        if self.isDead==True:
            SURFACE.blit(self.framesCurr_Arr[0],(self.x,self.y))
        else:
            SURFACE.blit(self.framesCurr_Arr[self.index],(self.x,self.y))
        
        
        