import brickpi
import time
import os
import time

interface=brickpi.Interface()
interface.initialize()

motors = [0,3]
speed = 1.0

interface.motorEnable(motors[0])
interface.motorEnable(motors[1])

LEFTMOTORPARAMS = interface.MotorAngleControllerParameters()
LEFTMOTORPARAMS.maxRotationAcceleration = 6.0
LEFTMOTORPARAMS.minPWM = 18.0
LEFTMOTORPARAMS.maxRotationSpeed = 12.0
LEFTMOTORPARAMS.feedForwardGain = 255/20.0
LEFTMOTORPARAMS.pidParameters.minOutput = -255
LEFTMOTORPARAMS.pidParameters.maxOutput = 255
LEFTMOTORPARAMS.pidParameters.k_p = 456.0
LEFTMOTORPARAMS.pidParameters.k_i = 250.0
LEFTMOTORPARAMS.pidParameters.k_d = 60.0

RIGHTMOTORPARAMS = interface.MotorAngleControllerParameters()
RIGHTMOTORPARAMS.maxRotationAcceleration = 6.0
RIGHTMOTORPARAMS.minPWM = 18.0
RIGHTMOTORPARAMS.maxRotationSpeed = 12.0
RIGHTMOTORPARAMS.feedForwardGain = 255/20.0
RIGHTMOTORPARAMS.pidParameters.minOutput = -255
RIGHTMOTORPARAMS.pidParameters.maxOutput = 255
RIGHTMOTORPARAMS.pidParameters.k_p = 444.0
RIGHTMOTORPARAMS.pidParameters.k_i = 100.0
RIGHTMOTORPARAMS.pidParameters.k_d = 60.0
interface.setMotorAngleControllerParameters(motors[0],LEFTMOTORPARAMS)
interface.setMotorAngleControllerParameters(motors[1],RIGHTMOTORPARAMS)

wheel_diam = 5.5
anti_lean_left = 1.01
anti_lean_right = 0.99

def timer():
   now = time.localtime(time.time())
   return now[5]

def go_straight(distance):
    angle = 2 * distance/wheel_diam
    left_angle = angle * anti_lean_left
    right_angle = angle * anti_lean_right
    interface.increaseMotorAngleReferences(motors,[left_angle,right_angle])

    while not interface.motorAngleReferencesReached(motors) :
    	motorAngles = interface.getMotorAngles(motors)
    	if motorAngles :
    		print "Motor angles: ", motorAngles[0][0], ", ", motorAngles[1][0]
    	time.sleep(0.1)

    print("Destination reached")


shaft_length = 13.6

def turn(angle):
    angle /= 2
    circumference = shaft_length * math.pi
    turn_size = circumference * angle / 360
    const_multip = 0.723
    turn_size *= const_multip
    interface.increaseMotorAngleReferences(motors,[turn_size, -turn_size])

    execute_turn();



    print("Turn DONE")

def execute_turn()

    while not (interface.motorAngleReferencesReached(motors) or current_sec = 2) :
    	motorAngles = interface.getMotorAngles(motors)
        current_sec = timer()
    	if motorAngles :
    		print "Motor angles: ", motorAngles[0][0], ", ", motorAngles[1][0]
    	time.sleep(0.1)

def Left90deg():
    turn(-90)

def Right90deg():
    turn(90)


#Right90deg()
#go_straight(40)
turn(90)
#go_straight(40)
turn(90)
#go_straight(40)
turn(90)
#go_straight(40)
turn(90)


#go_straight(300)




#turn(90)
#turn(90)

interface.terminate()
