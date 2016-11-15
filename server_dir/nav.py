#Imports, Globals
###################################

import time
import sys
import random
import robolib
from math import sin, cos, radians, degrees, atan2, sqrt, pi

bot = robolib.robolib()

bot_pos = [100, 100, 0] # (x,y,theta)

c = 0;

###################################



#Simulation Functions
###################################
def getRandomX():
    return random.gauss(0.0, 2)

def getRandomY():
    return random.gauss(0.0, 2)

def getRandomTheta(): 
    return random.gauss(0.0, 6)

def getStraightLine(botposition, dist):
    x = botposition[0] + (dist + getRandomX()) * cos(radians(botposition[2]))
    y = botposition[1] + (dist + getRandomY()) * sin(radians(botposition[2]))
    theta = botposition[2] + getRandomTheta()
    if len(botposition) == 3:
        return x, y, theta
    return x, y, theta, botposition[3]

def getRotation(botposition, angle):
    x = botposition[0]
    y = botposition[1]
    theta = botposition[2] + angle + getRandomTheta()
    if len(botposition) == 3:
        return x, y, theta
    return x, y, theta, botposition[3]


def directionTo(current_location, destination):
    dx = destination[0] - current_location[0]
    dy = destination[1] - current_location[1]
    angle = degrees(atan2(dy, dx))%360
    turn_angle = (angle - current_location[2])
    if turn_angle > 180:
        turn_angle -= 360
    elif turn_angle < -180:
        turn_angle += 360
        
    print(turn_angle)

    distance = sqrt(dx**2 + dy**2)
    return (distance, turn_angle, angle)


def navigateToWaypoint(start, destination):
    print("Destination: " + str(destination))
    
    distance, angle, absangle = directionTo(start, destination)

    after_turn = getRotation(start, angle)
    to_waypoint = getStraightLine(after_turn, distance)
    
    #final_x = to_waypoint[0] # x + cos(absangle) * distance
    #final_y = to_waypoint[1] #y + sin(absangle) * distance
    
    
    #line1 = (round(x, 5), round(y, 5), round(final_x, 5), round(final_y, 5))
    
    #print("drawLine:" + str(line1))
    #print("Navigating from: %f %f\t\tTO: %f %f" % (x, y, final_x, final_y))
    print("Navigating from", start, " to ", destination)
    print("Angle = ", angle)
    bot.turn(angle)
    if distance > 20:
        distance = 20
    bot.straight(distance)
    
    new_bot_pos = (start[0] + distance*cos(radians(absangle)), start[1]+ distance*sin(radians(absangle)), absangle)
        
    return new_bot_pos, distance, angle
    
    

        
###################################

#Commented code RIP
###################################
"""
def bunchOfEndpoints(bot_pos):
    measurements = []
    for _ in range(20):
        x = bot_pos[0] + getRandomX()
        y = bot_pos[1] + getRandomY()
        t = bot_pos[2] + getRandomTheta()
        
        measurements.append((x, y, t))
    
    return measurements


def interactiveNavigation():
    measurements = bunchOfEndpoints(bot_pos)
    
    print("Please enter new Wx, Wy coordinates for the bot. Correct format is: Wx,Wy")
    
    while True:
        wx, wy = input("Enter Wx,Wy: ")
        
        new_bot_pos = navigateToWaypoint(measurements, (int(wx), int(wy)))
        
        measurements = [new_bot_pos]
def naviTest():
    wayPoints = [(200, 150, 0), (200, 200, 180), (150, 200, 0), (150, 150, 0)]
    
    measurements = bunchOfEndpoints(bot_pos)

    navigateTo(measurements, bot_pos)    
    
    current_pos = bot_pos
    
    for wayPoint in wayPoints:
        distance, angle = navigateTo([current_pos], wayPoint)
        current_pos = wayPoint
        
    print("Navigating back: dist: %f, angle: %f" % (distance, angle))
"""



"""
def bunchOfEndpoints(bot_pos):
    all_particles = []
    endpoints = []
    
    def simulate_square(bot_pos, save_endpoints = False):
        bot_pos = getStraightLine(bot_pos, 10)
        all_particles.append(bot_pos)
        bot_pos = getStraightLine(bot_pos, 10)
        all_particles.append(bot_pos)
        bot_pos = getStraightLine(bot_pos, 10)
        all_particles.append(bot_pos)
        bot_pos = getStraightLine(bot_pos, 10)
        all_particles.append(bot_pos)
        bot_pos = getStraightLine(bot_pos, 10)
        all_particles.append(bot_pos)
        bot_pos = getRotation(bot_pos, -90)
        all_particles.append(bot_pos)
    
        if save_endpoints:
            endpoints.append(bot_pos)
    
        return bot_pos
    
    
    starting_pos = bot_pos
    for _ in range(20):
        bot_pos = starting_pos
        all_particles.append(starting_pos)
        bot_pos = simulate_square(bot_pos)
        bot_pos = simulate_square(bot_pos, True)
    
    #mapDraw(all_particles)
    print("drawParticles:"  + str(all_particles))

    return endpoints
"""

"""
        # Mapping Functions
    ###################################
    #constants used to map position to pixels
    CONV = 125.0/100.0 # conversion factor from distanec in mm into pixels
    ORIGIN = (210,610) # origin (0,0), +ve x to the right, +ve y upwards, +ve theta CCW
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
"""
###################################


