import robot
from robot import *

# CONFIGURATION
# This code configures robot's world
speed = 1
direction = 'east'
world = [[1,1,1,1,1,1,1,1,1,1],
         [1,2,0,0,0,0,0,0,0,1],
         [1,1,1,1,1,1,1,1,0,1],
         [1,0,0,0,0,0,0,1,0,1],
         [1,0,1,1,1,1,3,1,0,1],
         [1,0,1,1,1,1,1,1,0,1],
         [1,0,0,0,0,0,0,0,0,1],
         [1,1,1,1,1,1,1,1,1,1]]
robot.create(world, direction, speed)

# INSTRUCTIONS
# robot.turn_on()           Power on
# robot.turn_off()          Power off
# robot.forward()           Go forward
# robot.left()              Turn left
# robot.right()             Turn right
# robot.has_finished()      Returns True if game has finished
# robot.sense()             Sensor determines if there's a wall
#
# Start game and PRESS ENTER to active the robot

# Let's go!!
robot.turn_on()

# YOUR CODE HERE
robot.forward()

# Power off the robot
robot.turn_off()








