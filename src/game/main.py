'''
Created on May 14, 2015

@author: Kevin
'''
import pygame
import sys
import media
from mobs.bat import Bat
from media.HealthBar import healthBar
import game
from media.ammo import ammo
from game.engine import Engine
from pygame.locals import*
from mobs.bossBird import bossBird
from mobs.reloadBird import reloadBird
#from game.constants import*

#from engine import engine
  #######Load Media########
BACKGROUND = pygame.image.load("../media/background1.jpg")
LEFTBUTTON=1
CROSSHAIR = pygame.image.load("../media/crosshair.png")
CROSSHAIR.set_colorkey(game.constants.BLACK)
PISTOL = pygame.image.load("../media/pistol.png")

def main():
    
    #####Initializations
    pygame.init()
    pygame.font.init()
    
    pygame.mixer.init()
    font = pygame.font.Font(None,25)
    
    ###Fonts
    cmcsams = pygame.font.SysFont('comicsansms', 50, True, True)
    superFont = pygame.font.SysFont('comicsansms',100,True,True)
   
    
    FPS = 30
    FPS_CLOCK = pygame.time.Clock()
    
    SCREEN = pygame.display.set_mode(game.constants.WINDOW_SIZE)
    SCREEN.set_colorkey(game.constants.WHITE)
    
    ##UI setup
    playerAmmo = ammo()
    hpBar = healthBar()
    
    mobList =[]
    
    engine = Engine(mobList)
    pygame.mouse.set_visible(False)
    timer = 0
    seconds = 0
    minutes=0
    frame_count=0
    
     ########Game Loop##################
    while True:
        
        
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            #player shoots
            if event.type==pygame.MOUSEBUTTONUP and event.button==LEFTBUTTON:
            
                #Play the shot sound
                shootSound=pygame.mixer.Sound("../media/shoot.wav")
                shootSound.play()
                mob = engine.shoot(pygame.mouse.get_pos())
                #go through and check collisions
                if mob is None:
                   
                    playerAmmo.shoot()
                    
                else:
                    if mob.name=='reload':
                        
                        playerAmmo.reload()
                        
                    else:
                        if playerAmmo.bullets>0:
                            
                            playerAmmo.shoot()
                            mob.isDead=True
                            mob.die()
                            
            if pygame.mouse.get_focused():
                pos = pygame.mouse.get_pos()
                
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_DOWN:
                    hpBar.update()
                ###reload bird got triggered
                if event.key==pygame.K_r:
                    
                    
                    mobList.append(reloadBird())
                if event.key==pygame.K_a:
                    mobList.append(bossBird(0,0,2,0))  
        engine.turn(hpBar)
        
        
        draw(SCREEN)
        
        #Draw the Mobs
        for mob in mobList:
           
            mob.draw(SCREEN)
        
        playerAmmo.draw(SCREEN)    
        hpBar.draw(SCREEN)
         
        
        frame_count+=1
        total_seconds=frame_count//FPS
        minutes=total_seconds//FPS
        seconds=total_seconds%FPS
        output_string=" {0:02}:{1:02}".format(minutes, seconds)
        
        text = font.render(output_string,True,game.constants.SALMON)
            
        SCREEN.blit(text,(game.constants.WIDTH-60,game.constants.HEIGHT-25))
        text = cmcsams.render(str(engine.score),True,game.constants.CORAL)
        SCREEN.blit(text,(game.constants.WIDTH/2,game.constants.HEIGHT-80))
        if hpBar.width<1:
            drawEnd(SCREEN,engine.score,output_string,superFont)
            pygame.quit()
            sys.exit() 
        pygame.display.flip()
        FPS_CLOCK.tick(FPS)

def draw(SCREEN):
   

    SCREEN.convert()
    pos = pygame.mouse.get_pos()
    SCREEN.fill(game.constants.WHITE)
    SCREEN.blit(BACKGROUND,(0,0))
    
    SCREEN.blit(CROSSHAIR,(pos))    
   
####End game screen    
def drawEnd(SCREEN,score,timer,font):
    
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        
        scorestr = 'score:'+str(score)
        scoretxt = font.render(scorestr,True,game.constants.CORAL)
        timetxt = font.render('Time: '+timer,True,game.constants.SALMON)
    
        SCREEN.blit(scoretxt,(game.constants.WIDTH/4,game.constants.HEIGHT/2))
        SCREEN.blit(timetxt,(game.constants.WIDTH/4,game.constants.HEIGHT/4))
        pygame.display.flip()
    
if __name__== "__main__":
    main()
