import time
import sys
import random
import robolib
from math import sin, cos, radians

bot = robolib.robolib()

    
bot_pos = [600, 600, 180] # (x,y,theta)

c = 0;
def getRandomX():
    return random.gauss(0.0, 0.1)

def getRandomY():
    return random.gauss(0.0, 0.1)

def getRandomTheta(): 
    return random.gauss(0.0, 1.0)

numberOfParticles = 1

line1 = (10, 10, 10, 500) # (x0, y0, x1, y1)
line2 = (20, 20, 500, 200)  # (x0, y0, x1, y1)

print "drawLine:" + str(line1)
print "drawLine:" + str(line2)

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


all_particles = []

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
    bot_pos = getRotation(bot_pos, 90)
    all_particles.append(bot_pos)
    return bot_pos


starting_pos = bot_pos
for _ in range(20):
    bot_pos = starting_pos
    for _ in range(4):
        bot_pos = simulate_square(bot_pos)
    
print("X_diff: %f, Y_diff: %f" % (bot_pos[0] - starting_pos[0], bot_pos[1] - starting_pos[1]))
    
print("drawParticles:" + str(all_particles))

def do_square():
    #bot.straight(10)
    bot_pos[0] = bot_pos[0] - 150 + getRandomX()
    bot_pos[1] = bot_pos[1] + getRandomY()    
    particle = tuple(bot_pos)
    all_particles.append(particle)
    print("drawParticles: " + str(all_particles))
    
    #bot.straight(10)
    bot_pos[0] = bot_pos[0] - 150 + getRandomX()
    bot_pos[1] = bot_pos[1] + getRandomY()    
    particle = tuple(bot_pos)
    all_particles.append(particle)
    print("drawParticles: "  + str(all_particles))
    
    #bot.straight(10)
    bot_pos[0] = bot_pos[0] - 150 + getRandomX()
    bot_pos[1] = bot_pos[1] + getRandomY()    
    particle = tuple(bot_pos)
    all_particles.append(particle)
    print("drawParticles: "  + str(all_particles))
    
    #bot.straight(10)
    bot_pos[0] = bot_pos[0] - 150 + getRandomX()
    bot_pos[1] = bot_pos[1] + getRandomY()    
    particle = tuple(bot_pos)
    all_particles.append(particle)
    print("drawParticles: "  + str(all_particles))
    
    
print("All is done")

        
"""
while True:
    # Create a list of particles to draw. This list should be filled by tuples (x, y, theta).
    for i in range(3):
        particles = [tuple(bot_pos) for j in range(numberOfParticles)]
        print "drawParticles:" + str(particles)
        bot.straight(10)
        bot_pos[0] -= 10
        
        time.sleep(0.25)    
    c += 1
"""
