__all__ = []

import pygame, sys, os
from pygame.locals import *

import cafeinagame
from cafeinagame import *

import cafeinarobot

cr = None

# ENGLISH DEFINITIONS
def create(world, robot_direction, robot_velocity, out_X=0, out_Y=0):
    global cr
    cr = cafeinarobot.CafeinaRobot(world, robot_direction, robot_velocity, out_X, out_Y)

def turn_on():
    cr.turn_on()
 
def update():
    cr.update()
    cr.draw()

def forward():
    cr.forward()

def left():
    cr.turn_left()

def right():
    cr.turn_right()

def turn_off():
    cr.shutdown()

def sense():
    return cr.sense()

def has_finished():
    return cr.has_finished()

# SPANISH DEFINITIONS
def crear(world, robot_direction, robot_velocity, out_X=0, out_Y=0):
    cr = cafeinarobot.CafeinaRobot(world, robot_direction, robot_velocity, out_X, out_Y)

def encender():
    cr.turn_on()
 
def actualizar():
    cr.update()
    cr.draw()

def avanzar():
    cr.forward()

def izquierda():
    cr.turn_left()

def derecha():
    cr.turn_right()

def apagar():
    cr.shutdown()

def hay_muro():
    return cr.sense()

def ha_terminado():
    return cr.has_finished()
    
