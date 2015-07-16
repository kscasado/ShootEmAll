'''


@author: Kevin
'''
import pygame
import game
from mobs.mob import Mob
from media.SpriteSheet import SpriteSheet
class bossBird(Mob):
    framesL_Arr=[]
    framesC_Arr=[]
    framesR_Arr=[]
    framesM_Arr=[]
    def __init__(self,x,y,vx,vy):
        self.name='bossBird'
        self.isDead=False
        self.shooting=False
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.frames=4
        self.width=64
        self.height=64
        self.sheet=SpriteSheet('../media/blueBird.png'
                               ,12,384,384)
        
        self.index=0
        self.timer = 0
        
        for j in range(0,4):
            image = self.sheet.getImage(j*96,0,96,96,
                                               game.constants.WHITE)
            self.framesM_Arr.append(image)
                
        
        for j in range(0,4):
            image = self.sheet.getImage(j*96,2*96,96,96,
                                        game.constants.WHITE)
            self.framesR_Arr.append(image)
                
        
        for j in range(0,4):
            image = self.sheet.getImage(j*96,1*96,96,96,
                                        game.constants.WHITE)
            self.framesL_Arr.append(image)
        self.framesC_Arr=self.framesR_Arr
    def update(self):
        
        if self.timer%10==0:
            
            if self.index==self.frames-1:
                self.index=0
            else:
                    self.index+=1
                    ##check if you need to shoot
                    if self.framesC_Arr==self.framesM_Arr:
                        if self.index==3 and self.timer%3==0:
                             if self.isDead is False:
                                print('Bird Shot')
                                self.shooting=True
                        
        self.timer+=1
        self.x+=self.vx
        self.y+=self.vy
        if self.x>game.constants.WIDTH/4:
            if self.x<3*game.constants.WIDTH/4:
                if self.framesC_Arr !=self.framesM_Arr:
                    self.framesC_Arr=self.framesM_Arr
                    self.index=0
            elif self.vx>0 and self.x>3*game.constants.WIDTH/4:
                if self.framesC_Arr !=self.framesR_Arr:
                    self.framesC_Arr=self.framesR_Arr
                    self.index=0
        elif self.vx<0 and self.x<game.constants.WIDTH/4:
            if self.framesC_Arr !=self.framesL_Arr:
                self.framesC_Arr=self.framesL_Arr
                self.index=0
        self.checkWall()
        
    def checkWall(self):
        if(self.x+self.width>game.constants.WIDTH):
            self.vx=-self.vx
            self.framesC_Arr=self.framesL_Arr
            self.index=0
            self.update()
        if self.x<0:
            self.framesC_Arr=self.framesR_Arr
            self.index=0
            self.vx=-self.vx
            self.update()
        if self.y==(game.constants.HEIGHT-self.height):
            self.vy=0
    ### changes so the bird falls
    def isDead(self):
        self.vy=9
        self.vx=0
        self.isDead=True
    # check for a collision given the posistion
    def collide(self,pos):
        if self.x<pos[0] and self.x+self.width>pos[0] :
            
            if self.y<pos[1] and self.y+self.height>pos[1]:
               
                return True
        
        return False

    #####Draw to the screen    
    def draw(self,SURFACE):
        if self.isDead==True:
            SURFACE.blit(self.framesC_Arr[0],(self.x,self.y))
        else:
            SURFACE.blit(self.framesC_Arr[self.index],(self.x,self.y))
        
        
           
    