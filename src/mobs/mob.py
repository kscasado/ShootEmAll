'''
This is the parent mob class all mobs inherit from it and it is used 
for the master list in the game engine

@author: Kevin
'''

import pygame
class Mob(object):
    #reload = pygame.mixer.Sound("../media/reloadSound1.wav")
        
    def __init__(self):
        self.isDead=False
    def spriteCollide(self, mob1):
      # check for overlap 
      if self.x<mob1.x+mob1.width and self.x+self.width>mob1.x:
        
       
        if self.y<mob1.y+mob1.height and self.y+self.height>mob1.y:
            
            return True
    
        return False
    
    #update velocity and push back
    def collideUpdate(self):
        self.x-=self.vx
        self.vx=-self.vx
    def collide(self,pos):
        if self.x<pos[0] and self.x+self.width>pos[0] :
            
            if self.y<pos[1] and self.y+self.height>pos[1]:
               #self.reload.play()
               return True
        
        return False
    def die(self):
        self.vy=9
        self.vx=0
        self.isDead=True