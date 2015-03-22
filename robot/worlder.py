import pygame, sys, os
from pygame.locals import *

import cafeinagame
from cafeinagame import *

import types

class Worlder():
    def __init__(self, world_tiles, out_X, out_Y):
        self.content = content
        # Outter limits to build from lists a world
        self.out_X = out_X
        self.out_Y = out_Y
        self.robot_position = [0,0]
        self.objective_position = [0,0]
        self.world_tiles = world_tiles

    def build_world(self, world):       
        entities = []
        image = self.world_tiles[0]
        width = image.get_width()
        height = image.get_height()

        # Building the world
        # Initial y-position
        y = height * self.out_Y
        for row in world:
            # Reset x-position
            x = width * self.out_X
            for wall in row:
                # Set wall, robot or objective
                if wall == 1:
                    wallAnimation = cafeinagame.entities.Animation([image])
                    wallEntity = cafeinagame.entities.Entity(wallAnimation, [x,y])
                    entities.append(wallEntity)
                elif wall == 2:
                    self.robot_position = [x,y]
                elif wall == 3:
                    self.objective_position = [x,y]
                x += width
            y += height
        return entities

    def build_background(self, width, height):
        entities = []
        image = self.world_tiles[1]
        for x in range(0, width, image.get_width()):
            for y in range(0, width, image.get_height()):
                backAnimation = cafeinagame.entities.Animation([image])
                backEntity = cafeinagame.entities.Entity(backAnimation, [x,y])
                entities.append(backEntity)            
        return entities
        
        
        
        
