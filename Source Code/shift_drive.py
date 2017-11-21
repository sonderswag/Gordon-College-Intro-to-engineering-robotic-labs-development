from BrickPi import *
import pygame
from pygame.locals import * 
from time import sleep

import sys
 
#setting up the pygame screen and initiating pygame 
# there must be a screen to run pygame 
screen = pygame.display.set_mode((60,60))
pygame.font.init()
pygame.display.update()

# this is limiting the number of commands that are accepted by the programing for pygame 
pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN,pygame.KEYDOWN,pygame.QUIT])

# setting up the BrickPi and enabling the motors 
BrickPiSetup()
BrickPi.MotorEnable[PORT_A] = 1 
BrickPi.MotorEnable[PORT_B] = 1
BrickPiSetupSensors()

# setting up values 
up = 150
down = -up
turn = 100

# 273:"Up" ; 274:"Down" ; 276:"Left" ; 275:'Right ; 97 = a ; s = 115 ; w = 119 ; d = 100'

# this is the allowed keys that will be processed 
allow_keys =[119,115,97,100,32]

# this handles the assignment of values to the motors, it uses a python dictionary 
motor_down = {
    'motor_a':{
        119:up,
        115:down,
        97:-turn,
        100:turn,
        32:0
        
    },
    'motor_b':{
        119:up,
        115:down,
        97:turn,
        100:-turn,
        32:0

    }
}


while True: 
    # this updates the brickPi values 
    BrickPiUpdateValues()
    # this handles events form the keyboard 
    for event in pygame.event.get():
        # need this commmand to continue to get keyboard values 
        pygame.event.pump()
        # checking to see if a the event was a keydown 
        if event.type == pygame.KEYDOWN:
           key = event.key 
           # seeing if the key is a allowed value 
           if key in allow_keys:
               # seeing if the shift key is down. if down it will increase all the motor values by two 
               if event.mod == 1 :	
	           BrickPi.MotorSpeed[PORT_A] = 2*motor_down['motor_a'][key]
                   BrickPi.MotorSpeed[PORT_B] = 2*motor_down['motor_b'][key]
                   BrickPiUpdateValues()
               # when no shift key is pushed 
               else: 
               	   BrickPi.MotorSpeed[PORT_A] = motor_down['motor_a'][key]
                   BrickPi.MotorSpeed[PORT_B] = motor_down['motor_b'][key]
                   BrickPiUpdateValues()
    sleep(.05)