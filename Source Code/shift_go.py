from BrickPi import *
import pygame
from pygame.locals import * 
from time import sleep

import sys
 
#setting up the pygame screen and initiating pygame 
screen = pygame.display.set_mode((60,60))
pygame.font.init()


pygame.display.update()

# this is limiting the number of commands that are accepted by the programing for pygame 
pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN,pygame.KEYDOWN,pygame.QUIT])

# setting up the brickpi 
BrickPiSetup()

BrickPi.MotorEnable[PORT_A] = 1 
BrickPi.MotorEnable[PORT_B] = 1

# defing speeds 
up = 150
down = -up

# 273:"Up" ; 274:"Down" ; 276:"Left" ; 275:'Right ; 97 = a ; s = 115 ; w = 119 ; d = 100'

# filter for the dictionary 
allow_keys =[119,115,97,100,32]

# dictionary that handles the assignment of motor speeds 
# note will have to manully change the turning speeds in here 
motor_down = {
    'motor_a':{119:up,115:down,97:0,100:130,32:0},
    'motor_b':{119:up,115:down,97:130,100:0,32:0}
}

BrickPiSetupSensors()


# this is the main body of the program
while True: 
    BrickPiUpdateValues()
    for event in pygame.event.get():
        pygame.event.pump()
        if event.type == pygame.KEYDOWN:
           key = event.key 
           if key in allow_keys:
               if event.mod : # event.mod determines if the shift key is down. It returns true if it is being pressed 
                   BrickPi.MotorSpeed[PORT_A] = 2*motor_down['motor_a'][key]
                   BrickPi.MotorSpeed[PORT_B] = 2*motor_down['motor_b'][key] # this is simply doubling all the values being given by the dictionary. 
                   BrickPiUpdateValues()
               else: 
                   BrickPi.MotorSpeed[PORT_A] = motor_down['motor_a'][key]
                   BrickPi.MotorSpeed[PORT_B] = motor_down['motor_b'][key]
                   BrickPiUpdateValues()            
               
                         
    sleep(.05)