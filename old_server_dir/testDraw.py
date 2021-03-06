# Imports
###################################

import time
import sys
import random
import robolib
from math import sin, cos, radians

###################################

# Old Code
###################################
"""
def do_square():
    #bot.straight(10)
    bot_pos[0] = bot_pos[0] + getRandomX()
    bot_pos[1] = bot_pos[1] + getRandomY()    
    particle = tuple(bot_pos)
    all_particles.append(particle)
    #print("drawParticles: " + str(all_particles))
    
    #bot.straight(10)
    bot_pos[0] = bot_pos[0] + getRandomX()
    bot_pos[1] = bot_pos[1] + getRandomY()    
    particle = tuple(bot_pos)
    all_particles.append(particle)
    #print("drawParticles: "  + str(all_particles))
    
    #bot.straight(10)
    bot_pos[0] = bot_pos[0] + getRandomX()
    bot_pos[1] = bot_pos[1] + getRandomY()    
    particle = tuple(bot_pos)
    all_particles.append(particle)
    #print("drawParticles: "  + str(all_particles))
    
    #bot.straight(10)
    bot_pos[0] = bot_pos[0] + getRandomX()
    bot_pos[1] = bot_pos[1] + getRandomY()    
    particle = tuple(bot_pos)
    all_particles.append(particle)
    #print("drawParticles: "  + str(all_particles))
    return all_particles
"""
###################################

# Global Variables
###################################
bot = robolib.robolib()
    
bot_pos = [0, 0, 0] # [710,810,180]

c = 0;

numberOfParticles = 100

line1 = (10, 10, 10, 500) # (x0, y0, x1, y1)
line2 = (20, 20, 500, 200)  # (x0, y0, x1, y1)

all_particles = []


#constants used to map position to pixels
CONV = 125.0/100.0 # conversion factor from distanec in mm into pixels
ORIGIN = (210,610) # origin (0,0), +ve x to the right, +ve y upwards, +ve theta CCW
###################################

# Functions
###################################
def getRandomX():
    return random.gauss(0.0, 0.5)

def getRandomY():
    return random.gauss(0.0, 0.5)

def getRandomTheta(): 
    return random.gauss(0.0, 1)

# Simulation functions
###################################

def getStraightLine(botposition, dist):
    x = botposition[0] + (dist + getRandomX()) * cos(radians(botposition[2]))
    y = botposition[1] + (dist + getRandomY()) * sin(radians(botposition[2]))
    theta = botposition[2] + getRandomTheta()
    return x, y, theta

def getRotation(botposition, angle):
    x = botposition[0]
    y = botposition[1]
    theta = botposition[2] + angle + getRandomTheta()
    return x, y, theta

def simStraight(pos_list, dist):
    return [getStraightLine(pos, dist) for pos in pos_list]
def simRotate(pos_list, angle):
    return [getRotation(pos, angle) for pos in pos_list]


# Mapping functions
###################################

def mapPoint(pos):
    return (ORIGIN[0] + pos[0]*CONV, ORIGIN[1] - pos[1]*CONV, -pos[2])

def mapLine(line):
    return tuple([ORIGIN[i%2]+(-1)**(i%2)* line[i%4]*CONV for i in range(len(line))]) 

def mapDraw(point_list):  
    line1 = mapLine((0,0,400,0)) 
    line2 = mapLine((400,0,400,400))  
    line3 = mapLine((400,400,0,400))
    line4 = mapLine((0,400,0,0))

    print_particles = [mapPoint(pos) for pos in point_list]
    print "drawParticles: " + str(print_particles)
    print "drawLine:" + str(line1)
    print "drawLine:" + str(line2)
    print "drawLine:" + str(line3)
    print "drawLine:" + str(line4)

###################################

# Main Function
###################################

curr_list = [bot_pos for i in range(numberOfParticles)]
next_list = []

mapDraw(curr_list)

all_particles += curr_list
for side in range(4):
    for step in range(4):
        next_list = simStraight(curr_list, 100)
        all_particles += next_list
        curr_list = [i for i in next_list]
        bot.straight(10)
        time.sleep(0.5)
        mapDraw(curr_list)
        
    next_list = simRotate(curr_list, 90)
    all_particles += next_list
    curr_list = [i for i in next_list]
    bot.turn(90)
    time.sleep(0.5)
    mapDraw(curr_list)

print("X_diff: %f, Y_diff: %f" % (bot_pos[0] - starting_pos[0], bot_pos[1] - starting_pos[1]))
    
#print("drawParticles:" + str(all_particles))

#do_square()
#for i in range(len(all_particles)/100):
#    mapDraw(all_particles[0:100*i])
#    time.sleep(2)

print("All is done")
###################################
        

