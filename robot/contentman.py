import pygame, sys, os
from pygame.locals import *

import cafeinagame
from cafeinagame import *

import types

class ContentMan():
    def __init__(self, content):
        self.content = content
    
    def build_robot_animation(self, direction):
        images = self.content.load_images([['Robot-1-'+direction+'.bmp', (255,0,255)],
                                           ['Robot-2-'+direction+'.bmp', (255,0,255)]])
        return cafeinagame.entities.Animation(images, 120)

    def build_explotion(self):
        images = self.content.load_images([['Explode-0.bmp', (0,0,0)],
                                           ['Explode-1.bmp', (0,0,0)],
                                           ['Explode-2.bmp', (0,0,0)],
                                           ['Explode-1.bmp', (0,0,0)],
                                           ['Explode-2.bmp', (0,0,0)],
                                           ['Explode-3.bmp', (0,0,0)],                                           
                                           ['Explode-2.bmp', (0,0,0)],
                                           ['Explode-3.bmp', (0,0,0)],
                                           ['Explode-2.bmp', (0,0,0)],
                                           ['Explode-3.bmp', (0,0,0)],
                                           ['Explode-2.bmp', (0,0,0)],
                                           ['Explode-1.bmp', (0,0,0)],
                                           ['Explode-0.bmp', (0,0,0)]])
        animation = cafeinagame.entities.Animation(images, 120,False)
        return cafeinagame.entities.Entity(animation, [0,0])

    def build_objective(self, position):
        images = self.content.load_images([['Objective-1.bmp', (255,0,255)],
                                           ['Objective-2.bmp', (255,0,255)],])
        animation = cafeinagame.entities.Animation(images, 120)
        return cafeinagame.entities.Entity(animation, position)
        
        
        
        
