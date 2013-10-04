import pygame, sys, os
from pygame.locals import *

# Represents a basic logical and graphical
# object in the game
# Entity
class Entity:
    def __init__(self, animation, position):
        self.animation = animation
        self.position = position
        self.active = True

    def update(self, time):
        if not self.active:
            return
        self.animation.update(time, self.position)

    def draw(self, surface):
        if not self.active:
            return
        self.animation.draw(surface)

    _update = update
    _draw = draw

# Animation
class Animation:
    # Inits an animation
    def __init__(self, images, frametime=60, looping=True):
        self.frametime = frametime
        self.frame_count = len(images)
        self.images = images
        self.looping = looping
        self.elapsed_time = 0
        self.current_frame = 0
        self.active = True

    # Updates animation
    def update(self, time, position):
        # Updates position and time
        self.position = position
        self.elapsed_time += time

        # Updates frame if required
        if self.elapsed_time > self.frametime:
            self.current_frame += 1
            self.elapsed_time = 0
            # Looping ?
            if self.current_frame == self.frame_count:
                self.current_frame = 0;
                if not self.looping:
                    self.active = False;

    # Draws current frame
    def draw(self, screen):
        if not self.active:
            return
        screen.blit(self.images[self.current_frame], self.position)
