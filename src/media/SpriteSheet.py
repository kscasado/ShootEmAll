'''
Helper module used for creating and extracting the images from the sprite 
sheets
@author: Kevin
'''
import game
import pygame
class SpriteSheet(object):
    def __init__(self, name,numImages,width,height):
         
        self.sheet=pygame.image.load(name).convert()
        self.transColor=self.sheet.get_at((0,0))
        self.sheet.set_colorkey(self.transColor)
        self.size = numImages
        self.index = 0
        self.width = width
        self.height = height
    def nextImage(self):
        if self.index ==self.numImages:
            self.index = 0
        else:
            self.index+=1
        
            
    def getImage(self,x,y,width,height,color):
        image = pygame.Surface([width,
                                height]).convert()
        #transColor=image.get_at((0,0))
        image.blit(self.sheet,(0,0),(x,y,width,height))
        #image.convert_alpha()
        
        image.set_colorkey(game.constants.BLACK)    
        return image