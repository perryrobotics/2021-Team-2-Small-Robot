#!/usr/bin/python
import os, sys
import ctypes
from constants import *
from sensors import *
from movement import *
from effectors import *
from wait_for_start import *
from shut_down import *
import threading
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")
sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    
start_function = threading.Thread (target = shut_down)
KIPR.enable_servos()

#start position
KIPR.set_servo_position(ARM_SERVO, 1900)
KIPR.set_servo_position(ELBOW_SERVO, 2047)
claw_fullopen(50)
tail_up(50)
print("Press a to start the chg. diabetic stink!!")
while KIPR.a_button() == 0:
	pass
KIPR.msleep(2000) 
     
wait_for_start(3)
start_function.start()
#====================================================================================================
#Go Play Botball!!
back_to_black(900) 
forward(700,1175)
#Align to get the cupo thingy
right(900,1000)
backward(1100,700)
move_to_black(900) #tape at end of start box    
backward(900,1100)
left(850,1100)#turn to cup might need  to adjust
backward(1100,1550)
tail_down(50)
right(900, 90)

forward(1200, 2500)
left(340, 1420)
backward(1000,3770)	
tail_middle(50)
KIPR.msleep(50)

#tail_middle(50)
right(1000, 700)
left(1000,800)
forward(1200,4500)
right(1000,150)
forward(1200,2600)
backward(1200,1100)
left(1000,900)
forward(1000,4600)  #hit the pipe
backward(1000,300)
left(1000, 1050)
forward(1400,2000 )# start up the ramp
line_follow_bump(1000)
backward(1000,100)
left(1000, 800)
backward(1000, 2000)
#backward(500,300)
#=========================================================================================
#									FIRST DIP RUN!!
#=========================================================================================
move_servo_slow(ELBOW_SERVO, 2000, 10)
move_servo_slow(ARM_SERVO, 1750, 10)        
claw_closed(25)

line_follow_dist(1000, 6800)
KIPR.ao()


KIPR.mav(LMOTOR, 800)	#forward(1000,1550)      
#over mine
KIPR.mav(RMOTOR, 800)
while KIPR.analog(LINE_PORT_RIGHT) < THRESH:
	pass
KIPR.ao()
print ("Over mine!!")
#IN FRONT OF MINE
backward(600,500)
claw_fullopen(50)
move_servo_slow(ARM_SERVO, 1500, 10)
move_servo_slow(ELBOW_SERVO, 1500, 10)
move_servo_slow(ARM_SERVO, 400, 10)
forward(600, 160)
move_servo_slow(ELBOW_SERVO, 1580, 10)
forward(600,50)
move_servo_slow(ARM_SERVO, 10, 10)
claw_closed(10)
move_servo_slow(ARM_SERVO, 850, 10)
move_servo_slow(ELBOW_SERVO, 1200, 10)
        
backward(500, 2550) #CHANGED
move_servo_slow(ARM_SERVO, 1050, 10)
right(500,700)
backward(500,350)
left(500,1325)
forward(500,100)
#right(500,10)#CHANGE ON THE COMP DAY KEEP EITHER RIGHT OR LEFT TEST EVERY RUN EEEEEEEEEEEEEEEEEEE
#left(500,15) #CHANGE ON THE COMP DAY PSLPLSSPLSPLSPLPLSPLSPLSPLSPLS
move_servo_slow(ARM_SERVO, 530, 10)
forward(500,70)
claw_fullopen(5)
claw_closed(25)
#move_servo_slow(ARM_SERVO, 530, 20)
#move_servo_slow(ARM_SERVO, 505, 20)
#move_servo_slow(ARM_SERVO, 530, 20)
#move_servo_slow(ARM_SERVO, 505, 20)
right(500,100)
left(500,100)
claw_fullopen(15)
claw_closed(25)
move_servo_slow(ARM_SERVO, 1650, 10) 
move_servo_slow(ELBOW_SERVO, 2000, 10)
backward(800,150)
right(500,600)
KIPR.ao()

line_follow_dist(1000, 2250)
KIPR.mav(LMOTOR, 800)	#forward(1000,1550)      
#over mine
KIPR.mav(RMOTOR, 800)
while KIPR.analog(LINE_PORT_RIGHT) < THRESH:
	pass
KIPR.ao()
print ("Over mine!!")
backward(600,500)
#left(500,50)
claw_fullopen(50)
move_servo_slow(ARM_SERVO, 1500, 10)
move_servo_slow(ELBOW_SERVO, 1500, 10)
move_servo_slow(ARM_SERVO, 400, 10)
forward(600, 160)
move_servo_slow(ELBOW_SERVO, 1580, 10)
forward(600,50)
move_servo_slow(ARM_SERVO, 10, 10)
claw_closed(10)
move_servo_slow(ARM_SERVO, 850, 10)
move_servo_slow(ELBOW_SERVO, 1200, 10)
"""     
backward(500, 2550) #CHANGED
move_servo_slow(ARM_SERVO, 1050, 10)
right(500,700)
backward(500,350)
left(500,1325)
forward(500,100)
#left(500,80)
move_servo_slow(ARM_SERVO, 550, 10)
claw_fullopen(5)
claw_closed(25)
right(500,100)
left(500,100)
claw_fullopen(15)
claw_closed(25)
move_servo_slow(ARM_SERVO, 1650, 10) 
move_servo_slow(ELBOW_SERVO, 2000, 10)
backward(800,100)
right(500,600)
KIPR.ao()
"""
backward(1000, 3550)
claw_fullopen(50)
#IF CRAB ROBOT WORKS

            
	