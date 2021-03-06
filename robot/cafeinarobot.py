import pygame, sys, os
from pygame.locals import *

import cafeinagame
from cafeinagame import *

from .contentman import ContentMan
from .worlder import Worlder
from .robot import Robot

import random

class CafeinaRobot:
    # Init game
    def __init__(self, world, robot_direction, robot_velocity,out_X=0, out_Y=0):
        TILE_SIZE = 80
        self.game = cafeinagame.game.Game()
        self.game.init_video('Cafeina Robot')

        # Load content
        content = cafeinagame.content.Content('Content/')
        contentman = ContentMan(content)
             
        # Load world        
        world_tiles = contentman.load_world_tiles()
        worlder = Worlder(world_tiles, out_X, out_Y)  
        self.world = worlder.build_world(world)

         # Load robot        
        animations = [contentman.load_robot_animation('north'),
                      contentman.load_robot_animation('east'),
                      contentman.load_robot_animation('south'),
                      contentman.load_robot_animation('west')]
        self.robot = Robot(animations, worlder.robot_position, robot_direction, robot_velocity, TILE_SIZE)

        # Load objective
        self.objective = contentman.load_objective_animation(worlder.objective_position)

        # Create background
        self.background = worlder.build_background(self.game.width, self.game.height)

        # Load explotion
        self.explotion = contentman.load_explotion_animation()        
        
        # Add managed entities to game
        # this will auto-update and draw them
        self.game.add_entity(self.robot, 0)
        self.game.add_entity(self.objective, 0)        
        self.game.add_entities(self.world, 1)
        self.game.add_entities(self.background, 10)

        # State
        self.state = 'pause'

    # Updates all game
    def update(self):
        if not self.game.active:
            return
        # Process input
        self.process_input(self.game.get_events())        
        # Update game
        self.game.update()

    # Draws all game
    def draw(self):
        # Draw game
        self.game.draw()

    # Executes gamecyles when moving   
    def gamecycle_moving(self):
        while not self.robot.has_valid_position() or self.state == 'pause':
            self.gamecycle()

    # Update and draw
    def gamecycle(self):
        self.update()
        self.draw()

    # Start!
    def turn_on(self):
        self.gamecycle_moving()        

    # Robot -> Forward    
    def forward(self):
        if self.robot.sense(self.world):
            self.explode()
            self.shutdown()
            return
        self.robot.forward()
        self.gamecycle_moving()
        if self.has_finished():
            return        

    # Robot -> Left
    def turn_left(self):
        self.robot.turn_left()
        self.gamecycle_moving()
    
    # Robot -> Right
    def turn_right(self):
        self.robot.turn_right()
        self.gamecycle_moving()
    
    # Robot -> Shutdown
    def shutdown(self):
        self.game.finalize()
    
    # Robot -> Sense
    def sense(self):
        return self.robot.sense(self.world)

    # Robot -> has finished ?
    def has_finished(self):
        if not self.robot.has_finished(self.objective):
            return False
        self.objective.animation.active = False
        self.gamecycle()
        return True        

    # Exploding sequence
    def explode(self):
        for i in range(20):
            self.robot.forward()
            self.gamecycle()
                
        self.explotion.position = [self.robot.position[0],self.robot.position[1]]
        self.game.add_entity(self.explotion, 0)
        self.robot.animation.active = False
        while self.explotion.animation.active:
            self.gamecycle()

    # Process al events
    def process_input(self, events):
        for event in events: 
            if event.type == QUIT: 
                self.game.finalize()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.game.finalize_event()
                elif event.key == K_RETURN:                    
                    self.change_state()

    def change_state(self):
        if self.state == 'play':
            self.state = 'pause'
        else:
            self.state = 'play'
        print(self.state)
        
                
