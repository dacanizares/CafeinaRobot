import pygame, sys, os
from pygame.locals import *

import cafeinagame
from cafeinagame import *

import types

class ContentMan():
    def __init__(self, content):
        self.content = content
    
    def load_robot_animation(self, direction):
        images = self.content.load_images([['Robot-1-'+direction+'.bmp', (255,0,255)],
                                           ['Robot-2-'+direction+'.bmp', (255,0,255)]])
        return cafeinagame.entities.Animation(images, 120)

    def load_explotion_animation(self):
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

    def load_objective_animation(self, position):
        images = self.content.load_images([['Objective-1.bmp', (255,0,255)],
                                           ['Objective-2.bmp', (255,0,255)],])
        animation = cafeinagame.entities.Animation(images, 120)
        return cafeinagame.entities.Entity(animation, position)

    def load_world_tiles(self):
        return self.content.load_images([["Wall.bmp"],["Back.bmp"]])
        
        
        
        
