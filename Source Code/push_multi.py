from BrickPi import *
import pygame
from pygame.locals import * 
from time import sleep

import sys
 
#setting up the pygame screen and initiating pygame, screen must be here 
screen = pygame.display.set_mode((60,60))
pygame.font.init()
pygame.display.update()

# this is limiting the number of commands that are accepted by the programing for pygame 
pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN,pygame.KEYDOWN,pygame.QUIT])

# setting up the brickpi motors 
BrickPiSetup()
BrickPi.MotorEnable[PORT_A] = 1 
BrickPi.MotorEnable[PORT_B] = 1

up = 150
down = -up
left_motor_a = 70
right_motor_a = 130
left_motor_b = right_motor_a
right_motor_b = left_motor_a
BrickPiSetupSensors()

# 273:"Up" ; 274:"Down" ; 276:"Left" ; 275:'Right ; 97 = a ; s = 115 ; w = 119 ; d = 100'

# list of allowed keys (need to add if more are needed)
allow_keys =[119,115,97,100,32] 

# handles the setting of motors speeds 
motor_a = {
    0:{119:up,115:down,97:left_motor_a,100:right_motor_a,32:0},
    1:{119:up+30,115:down-30,97:left_motor_a-20,100:right_motor_a+20,32:0},
    2:{119:up+70,115:down-70,97:left_motor_a-60,100:right_motor_a+50,32:0},
    3:{119:up+110,115:down-110,97:left_motor_a-150,100:right_motor_a+70,32:0}     
    }
motor_b = {
    0:{119:up,115:down,97:left_motor_b,100:right_motor_,32:0},
    1:{119:up + 30,115:down-30,97:left_motor_b+20,100:right_motor_b-20,32:0},
    2:{119:up+70,115:down -70,97:left_motor_b+60,100:right_motor_b-60,32:0},
    3:{119:up+110,115:down-110,97:left_motor_b+70,100:right_motor_b-150,32:0}
    }



# some needed variables that handles the counting 
num = 0
last_key = 50 

# this is a funciton that counts how many times in a row a key has been pressed> 
# the maximum number that this function will return is 3 
def count(count,key,last_key):
    #print key 
    #print last_key
    if count == 3: # setting the limit of the number of key presses
        count = 2
    if last_key == key: 
        count +=1 
    else: 
        count = 0
        
    last_key = key 	
    return count,last_key
    
# this is the main while loop:
while True: 
    BrickPiUpdateValues()
    
    # this loop handles getting the keys that have been pressed. 
    for event in pygame.event.get():
        pygame.event.pump()
        if event.type == pygame.KEYDOWN:
           key = event.key 
           num,last_key = count(num,key,last_key)
           #print num 
           if key in allow_keys: # if the key that has been pressed is allowed. 
               # the statement on the right side of the equals sign, grabs a value from the dictionary above. 
               BrickPi.MotorSpeed[PORT_A] = motor_a[num][key]
               BrickPi.MotorSpeed[PORT_B] = motor_b[num][key]
               BrickPiUpdateValues()
    sleep(.05)