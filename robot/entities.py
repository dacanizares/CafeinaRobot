import pygame, sys, os
from pygame.locals import *

import cafeinagame
from cafeinagame import *

import types

class Robot(cafeinagame.entities.Entity):
    def __init__(self, animations, position, direction, velocity, size):
        self.animations = animations
        self.directions = ['north', 'east', 'south', 'west']
        self.position = position
        self.direction = direction
        self.size = size 
        self.active = True
        self.velocity = velocity

    def update(self, time):
        if not self.x_valid():
            self.forward()
        if not self.y_valid():
            self.forward()

        self.animation = self.animations[self.get_direction_index()]
        self._update(time)

    def draw(self, surface):        
        self._draw(surface)

    def sense(self, world):
        x = int(self.position[0])
        y = int(self.position[1])
        if self.direction == 'east':
            x += self.size
        if self.direction == 'west':
            x -= self.size
        if self.direction == 'north':
            y -= self.size 
        if self.direction == 'south':
            y += self.size
        matches = [wall for wall in world if wall.position[0] == x and wall.position[1] == y]
        return len(matches) > 0

    def forward(self):
        if self.direction == 'east':
            self.position[0] += self.velocity
        if self.direction == 'west':
            self.position[0] -= self.velocity
        if self.direction == 'north':
            self.position[1] -= self.velocity
        if self.direction == 'south':
            self.position[1] += self.velocity

    def has_finished(self, objective):
        return self.position == objective.position

    def turn_left(self):
        index = (self.get_direction_index() - 1) % 4
        self.direction = self.directions[index]
        
    def turn_right(self):
        index = (self.get_direction_index() + 1) % 4
        self.direction = self.directions[index]
        
    def get_direction_index(self):
        return self.directions.index(self.direction)

    def has_valid_position(self):
        return self.x_valid() and self.y_valid()

    def x_valid(self):
        return self.position[0] % self.size == 0

    def y_valid(self):
        return self.position[1] % self.size == 0


class Worlder():
    def __init__(self, content, out_X, out_Y):
        self.content = content
        # Outter limits to build from lists a world
        self.out_X = out_X
        self.out_Y = out_Y
        self.robot_position = [0,0]
        self.objective_position = [0,0]

    def build_world(self, world):
        if isinstance(world, types.ListType):
            return self.build_world_lst(world)
        else:
            return self.build_world_str(world)
            
    
    def build_world_lst(self, world):
        entities = []
        image = self.content.load_image('Wall.bmp')
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
        
        
    def build_world_str(self, world):
        if world == '':
            return []
        entities = []
        walls = world.split('#')
        image = self.content.load_image('Wall.bmp')
        for wall in walls:
            positionXY = wall.split(';')
            x = int(positionXY[0])
            y = int(positionXY[1])

            wallAnimation = cafeinagame.entities.Animation([image])
            wallEntity = cafeinagame.entities.Entity(wallAnimation, [x,y])
            entities.append(wallEntity)            
        return entities

    def build_background(self, width, height):
        entities = []
        image = self.content.load_image('Back.bmp')
        for x in range(0, width, image.get_width()):
            for y in range(0, width, image.get_height()):
                backAnimation = cafeinagame.entities.Animation([image])
                backEntity = cafeinagame.entities.Entity(backAnimation, [x,y])
                entities.append(backEntity)
            
        return entities

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
        
        
        
        
