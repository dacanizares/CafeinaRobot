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
