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

numberOfParticles = 1

line1 = (10, 10, 10, 500) # (x0, y0, x1, y1)
line2 = (20, 20, 500, 200)  # (x0, y0, x1, y1)

all_particles = []

###################################

# Functions
###################################
def getRandomX():
    return random.gauss(0.0, 0.1)

def getRandomY():
    return random.gauss(0.0, 0.1)

def getRandomTheta(): 
    return random.gauss(0.0, 1.0)



#function that converts position values in cm into pixel dist
#current conversion factor is 100mm to 150px 
def map_draw(point_list):
    conv = float(150.0/100.0)
    x0 = 210
    y0 = 710
    
    #draw the square frame to initialize
    #following the 2D coordinate frame specified in the first practical
    #(0,0) is at the bottom right, with +ve x to the right, +ve y upwards    
    line1 = (x0, y0, x0 + 400*conv, y0) # 
    line2 = (x0 + 400*conv, y0,x0 + 400*conv, y0 - 400*conv)  
    line3 = (x0 + 400*conv, y0 - 400*conv, x0, y0 - 400*conv)
    line4 = (x0, y0 - 400*conv, x0, y0)
    
    def pxpos(pos_tuple):
        px_x = x0 + pos_tuple[0]*conv
        px_y = y0 + pos_tuple[1]*conv
        return px_x, px_y, pos_tuple[2]

    print_particles = [pxpos(pos) for pos in point_list]
    print("drawParticles: " + str(print_particles))
    print "drawLine:" + str(line1)
    print "drawLine:" + str(line2)
    print "drawLine:" + str(line3)
    print "drawLine:" + str(line4)


#print "drawLine:" + str(line1)
#print "drawLine:" + str(line2)

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


def simulate_square(bot_pos):
    #print("Starting position: " + str(starting_pos))
    
    bot_pos = getStraightLine(bot_pos, 100)
    all_particles.append(bot_pos)
    bot_pos = getStraightLine(bot_pos, 100)
    all_particles.append(bot_pos)
    bot_pos = getStraightLine(bot_pos, 100)
    all_particles.append(bot_pos)
    bot_pos = getStraightLine(bot_pos, 100)
    all_particles.append(bot_pos)
    bot_pos = getRotation(bot_pos, -90)
    all_particles.append(bot_pos)
    return bot_pos


###################################

# Main Function
###################################
starting_pos = bot_pos
for _ in range(10000):
    bot_pos = starting_pos
    for _ in range(4):
        bot_pos = simulate_square(bot_pos)

        
print("X_diff: %f, Y_diff: %f" % (bot_pos[0] - starting_pos[0], bot_pos[1] - starting_pos[1]))
    
#print("drawParticles:" + str(all_particles))

#do_square()
map_draw(all_particles)

print("All is done")
###################################
        

