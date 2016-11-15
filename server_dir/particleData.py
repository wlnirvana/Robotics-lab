#!/usr/bin/env python 

# Some suitable functions and data structures for drawing a map and particles

import time
import random
import math
import helperFunctions as hf
import nav

all_waypoints = [(84, 30), (180, 30), (180, 54), (138, 54), (138, 168), (114, 168), (114, 84), (84, 84), (84, 30)]

# Functions to generate some dummy particles data:
def calcX():
    return random.gauss(50,10) # in cm

def calcY():
    return random.gauss(140,3) # in cm

def calcW():
    return random.random()

def calcTheta():
    return 0


# A Canvas class for drawing a map and particles:
#     - it takes care of a proper scaling and coordinate transformation between
#      the map frame of reference (in cm) and the display (in pixels)
class Canvas:
    def __init__(self,map_size=210):
        self.map_size    = map_size;    # in cm;
        self.canvas_size = 768;         # in pixels;
        self.margin      = 0.05*map_size;
        self.scale       = self.canvas_size/(map_size+2*self.margin);

    def drawLine(self,line):
        x1 = self.__screenX(line[0]);
        y1 = self.__screenY(line[1]);
        x2 = self.__screenX(line[2]);
        y2 = self.__screenY(line[3]);
        print "drawLine:" + str((x1,y1,x2,y2))

    def drawParticles(self,data):
        display = [(self.__screenX(d[0]),self.__screenY(d[1]),-d[2], d[3]) for d in data];
        print "drawParticles:" + str(display);

    def __screenX(self,x):
        return (x + self.margin)*self.scale

    def __screenY(self,y):
        return (self.map_size + self.margin - y)*self.scale

# A Map class containing walls
class Map:
    def __init__(self):
        self.walls = [];

    def add_wall(self,wall):
        self.walls.append(wall);

    def clear(self):
        self.walls = [];

    def draw(self):
        for wall in self.walls:
            canvas.drawLine(wall);
    def getWalls(self):
        return self.walls

# Simple Particles set
class Particles:
    def __init__(self, mymap, pos=None):
        self.n = 40;
        weight = 1/self.n;
        self.mean = [0,0,0] 
        if pos == None:

            self.data =  [(calcX(), calcY(), calcTheta(), calcW()) for i in range(self.n)]
        else:
            self.data = [(pos[0], pos[1], pos[2], weight) for _ in range(self.n)]

        self.mymap = mymap


    def update(self, z):
        weight_list = []
        
        #calculates the new weights for each particle based on a sonar reading
        for particle in self.data:
            dist = hf.calcEstTruth(particle[0],particle[1],particle[2], self.mymap)
            prob = hf.calculate_likelihood(dist, z)
            weight_list.append(prob)
        
        #normalizing the weights of each particle
        total_weight = sum(weight_list)
        self.data = [ (p[0],p[1],p[2],w/total_weight) for p,w in zip(self.data,weight_list)]

        
        
    def resample(self):
        sample_array = []
        new_particles = []
        for n in range(self.n):
            for x in range(int(self.data[n][3]*100)):
                sample_array.append(n)
        for n in range(self.n):
            index = random.choice(sample_array)
            new_particles.append((self.data[index][0], self.data[index][1], self.data[index][2], (1.0/(self.n))))
        self.data = new_particles    
        
        #calculating mean from new samples
        self.mean = [0,0,0]
        for n in range(self.n):
            self.mean[0] += self.data[n][0]*self.data[n][3]
            self.mean[1] += self.data[n][1]*self.data[n][3]
            self.mean[2] += self.data[n][2]*self.data[n][3]
        return tuple(self.mean)
        
    '''            
    #            closestDistance = -1
    #            closestwall = None

                for wall in self.mymap.walls:
                    A = (wall[0], wall[1])
                    B = (wall[2], wall[3])

                    m = hf.frontalDistance(A, B, particle)
                    intsect = hf.intersection(particle, m)
                    if wallInFront(A, B, intsect, m):
                        if closestDistance == -1 or closestDistance > m:
                            closestDistance = m
                            #closestwall = wall


    #            distDelta = abs(
    #            if closestDistance >= 0:
    #                hf.likelyhood0-
    #                distDiffs.append()
    #            else:
    #                distances.append(0)
    '''

    def straight(self, dist):
        self.data = [nav.getStraightLine(p,dist) for p in self.data]
        
    def turn(self, angle):
        self.data = [nav.getRotation(p,angle) for p in self.data]
        
        
    def get(self, index):
        return self.data[index]
    
    def draw(self):
        canvas.drawParticles(self.data);

        
def plotWaypoints(waypoints):
    for point in waypoints:
        x,y = point
        canvas.drawLine((x-5,y-5,x+5,y+5))
        canvas.drawLine((x+5,y-5,x-5,y+5))
        
canvas = Canvas();    # global canvas we are going to draw on

mymap = Map();
# Definitions of walls
# a: O to A
# b: A to B
# c: C to D
# d: D to E
# e: E to F
# f: F to G
# g: G to H
# h: H to O
mymap.add_wall((0,0,0,168));        # a
mymap.add_wall((0,168,84,168));     # b
mymap.add_wall((84,126,84,210));    # c
mymap.add_wall((84,210,168,210));   # d
mymap.add_wall((168,210,168,84));   # e
mymap.add_wall((168,84,210,84));    # f
mymap.add_wall((210,84,210,0));     # g
mymap.add_wall((210,0,0,0));        # h
mymap.draw();
plotWaypoints(all_waypoints)



#particles = Particles(mymap.getWalls());

def smartNav():
    start = all_waypoints[0]
    next_start = (all_waypoints[0][0], all_waypoints[0][1],0)
    OFFSET = 6
    particles = Particles(mymap.getWalls(), (84,30,0));
    reading = sum([nav.bot.readUltrasound() for i in range(10)])/10
    particles.update(reading+OFFSET)
    bot_pos = particles.resample()
    particles.draw()
    
    ind = 1
    while ind < len(all_waypoints):
        checkpoint = all_waypoints[ind]
        new_pos, distance, angle = nav.navigateToWaypoint(bot_pos,checkpoint)
        reading = sum([nav.bot.readUltrasound() for i in range(10)])/10
        
        particles.turn(angle)
        particles.straight(distance)
        
        particles.update(reading+OFFSET)
        bot_pos = particles.resample()
        print bot_pos
        particles.draw()
        
        if (checkpoint[0]-new_pos[0])**2 + (checkpoint[1]- new_pos[1])**2 < 9:
            ind += 1
            
        
        
        
        

#nav.bot.straight(50) 
smartNav()
'''
    #t = 0;
    z = 20
    while z < 25:
        print'sonar reading = ', z
        particles.update(z)
        particles.draw()
        particles.resample()
        particles.get_point()
        time.sleep(2)
        z += 1
'''