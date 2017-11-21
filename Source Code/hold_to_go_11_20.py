import pygame
from pygame.locals import * 
from time import sleep
from BrickPi import * 

# this starts the pygame, there must be a screen in order for it to work 
pygame.init()
screen = pygame.display.set_mode((60,60))
pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN,pygame.KEYUP,pygame.KEYDOWN])

# this starts up the brickpi
BrickPiSetup()
BrickPi.MotorEnable[PORT_A] = 1 
BrickPi.MotorEnable[PORT_B] = 1
BrickPiSetupSensors()


# this sets some valus 
up = 150
down = -up
turn = 150 

# 273:"Up" ; 274:"Down" ; 276:"Left" ; 275:'Right ; 97 = a ; s = 115 ; w = 119 ; d = 100'

# list of allowed keys 
allow_keys =[273,274,276,275]

#this handles the assignment of speeds motors 
motor_down = {
    'motor_a':{
        273:up,
        274:down,
        275:turn,
        276:-turn
        
    },
    'motor_b':{
        273:up,
        274:down,
        275:-turn,
        276:turn

    }
}

motor_up = {
    'motor_a':{
        273:0,
        274:0,
        275:0,
        276:0
    },
    'motor_b':{
        273:0,
        274:0,
        275:0,
        276:0
    }
}


while True: 
     # this handles getting events form the keyboard 
     for event in pygame.event.get(): 
         # checks to see if the key is pushed down 
         if event.type == pygame.KEYDOWN:
             key = event.key 
             # sees the if the key pressed is a allowed key 
             if key in allow_keys:
                 BrickPi.MotorSpeed[PORT_A] = motor_down['motor_a'][key]
                 BrickPi.MotorSpeed[PORT_B] = motor_down['motor_b'][key]
                 BrickPiUpdateValues()
         # this handles the key being let up and which will stop the motor      	
         elif event.type == pygame.KEYUP:
             key = event.key 
             if key in allow_keys: 
                           	 
                 BrickPi.MotorSpeed[PORT_A] = motor_down['motor_a'][key]
                 BrickPi.MotorSpeed[PORT_B] = motor_down['motor_b'][key]
   		 BrickPiUpdateValues()
         
     sleep(.1)                 
               
        
