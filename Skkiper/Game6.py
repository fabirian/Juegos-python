'''
Created on 29/09/2022

@author: fabian
'''

import sys
import cfg
import pygame
import random
from jedi.third_party.typeshed.stdlib.2.string import center

class SkierClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.direction = 0
        self.imagepaths = cfg.SKIER_IMAGE_PATHS[:-1]
        self.image = pygame.image.load(self.imagepaths[self.direction])
        self.rect = self.image.get_rect()
        self.rect.center = [320, 100]
        self.speed = [self.direction, 6-abs(self.direction)*2]
        
        def turn(self, num):
            self.direction += num
            self.direction = max(-2, self.direction)
            self.direction = min(2, self.direction)
            
            center = self.rect.center
            self.image = pygame.image.load(self.imagepaths[self.direction])
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.speed = [self.direction, 6-abs(self.direction)*2]
            return self.speed
        
        def  move(self):
            self.rect.centerx += self.speed[0]
            self.rect.centerx = max(20, self.rect.centerx)
            self.rect.centerx = min(620, self.rect.centerx)
            
        def setFall(self):
            self.image = pygame.image.load(cfg.SKIER_IMAGE_PATHS[-1])
            
        def setForward(self):
            self.direction
            self.image = pygame.image.load(self.imagepaths[self.direction])
        

class ObstacleClass(pygame.sprite.Sprite):
    def __init__(self, img_path, location, attribute):
        pygame.sprite.Sprite.__init__(self)
        