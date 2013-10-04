__all__ = ["entities", "cafeinarobot"]

import pygame, sys, os
from pygame.locals import *

import cafeinagame
from cafeinagame import *

import cafeinarobot

class state:
    def __init__(self):
        return


s = state()

# ENGLISH DEFINITIONS
def create(world, robot_direction, robot_velocity, robot_position=None, objective_position=None,out_X=0, out_Y=0):
    s.cr = cafeinarobot.CafeinaRobot(world, robot_direction, robot_velocity, robot_position, objective_position,out_X, out_Y)

def configure(posicion_robot, direccion_robot, velocidad_robot, posicion_objetivo, muros):
    s.cr = cafeinarobot.CafeinaRobot(muros, direccion_robot, velocidad_robot, posicion_robot, posicion_objetivo,0,0)

def turn_on():
    s.cr.turn_on()
 
def update():
    s.cr.update()
    s.cr.draw()

def forward():
    s.cr.forward()

def left():
    s.cr.turn_left()

def right():
    s.cr.turn_right()

def turn_off():
    s.cr.shutdown()

def sense():
    return s.cr.sense()

def has_finished():
    return s.cr.has_finished()

# SPANISH DEFINITIONS
def crear(world, robot_direction, robot_velocity, robot_position=None, objective_position=None,out_X=0, out_Y=0):
    s.cr = cafeinarobot.CafeinaRobot(world, robot_direction, robot_velocity, robot_position, objective_position,out_X, out_Y)

def configurar(posicion_robot, direccion_robot, velocidad_robot, posicion_objetivo, muros):
    s.cr = cafeinarobot.CafeinaRobot(muros, direccion_robot, velocidad_robot, posicion_robot, posicion_objetivo,0,0)

def encender():
    s.cr.turn_on()
 
def actualizar():
    s.cr.update()
    s.cr.draw()

def avanzar():
    s.cr.forward()

def izquierda():
    s.cr.turn_left()

def derecha():
    s.cr.turn_right()

def apagar():
    s.cr.shutdown()

def hay_muro():
    return s.cr.sense()

def ha_terminado():
    return s.cr.has_finished()
    
