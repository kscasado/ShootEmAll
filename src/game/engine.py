'''
This Module is to simulate one full turn and do any of the collision
checking neccessary for the game. It also keeps track of the Score and time

@author: Kevin
'''
import pygame
import game
import random
from mobs.bossBird import bossBird
from mobs.reloadBird import reloadBird
from mobs.bat import Bat
class Engine(object):
    
    def __init__(self,mobGroup):
        self.score=0
        self.mobGroup = mobGroup
        self.timer=0
        self.frequency=100
    ## decide to spawn an enemy reduce change frequencies
    def tick(self):
        self.timer+=1
        
        y = random.randrange(1,4)
        if y<2:
            
            if self.timer%self.frequency/4==0:
                print('added bat')
                self.mobGroup.append(Bat(0,y*64,4,0))
        if y>=2:
            if self.timer%self.frequency/10==0:
                print('added boss')
                self.mobGroup.append(bossBird(0,y*64,4,0))
            
        if self.timer%1000==0:
            self.frequency-=1
    #check if there are any colisssions with the mouse and the mob group
    def checkCollide(self,pos=(0,0)):
    
        for mob in self.mobGroup:
            if mob.collide(pos):
                if mob.name!='reload':
                    
                    self.score+=10
                print('killed!')
                mob.die()
                
                
        for mob1 in self.mobGroup:
            for mob2 in self.mobGroup:
                if mob1.spriteCollide(mob2):
                    if mob1!=mob2:
                        mob1.collideUpdate()
                        mob2.collideUpdate()
    # Go through one full turn
    def turn(self,healthBar):
        for mob in self.mobGroup:
            mob.update()
            if mob.name=='bossBird':
                if mob.shooting==True:
                    crowSound  = pygame.mixer.Sound("../media/crowShoot.wav")
                    crowSound.play()
                    mob.shooting=False
                    healthBar.update()
            if mob.isDead==True:
                
                
                if mob.y>=(game.constants.HEIGHT-mob.height) :
                    
                    self.mobGroup.remove(mob)
        self.checkCollide()
        self.tick()
        
    def shoot(self,pos):
        for mob in self.mobGroup:
            if mob.collide(pos):
                if mob.name=='reload':
                    print('reload hit')
                    
                else:
                    self.score+=10
                #mob.die()
                return mob
        return None