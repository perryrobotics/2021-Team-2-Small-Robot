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
KIPR.set_servo_position(ARM_SERVO, 1450)
KIPR.set_servo_position(ELBOW_SERVO, 2047)
claw_fullopen(50)
tail_up(50)
print("Press a to start the chg. diabetic!!")
while KIPR.a_button() == 0:
	pass
KIPR.msleep(2000) 
     
wait_for_start(1)
start_function.start()
#====================================================================================================
#Go Play Botball!!
forward(1000, 2500)
claw_halfopen(50)
arm_back(50)
backward(900, 2800)
claw_fullopen(50)  # scored the cube
backward(900, 300) #back towards cup

#Align to get the cupo thingy
right(900,1000)
backward(900,600)
backward(400,700)
move_to_black(900) #tape at end pof sdtart box    
backward(900,1100)
left(900,1100)#turn to cup might need  to adjust
backward(900,1550)
tail_down(50)
right(900, 90)

forward(1000, 2500)
left(400, 1000)
backward(1000,4350)	
#tail_up(50)
tail_middle(50)
right(1000, 700)
left(1000,800)
forward(1000,4500)
right(1000,290)
forward(1000,2600)
backward(1000,1200)
left(1000,900)

forward(1000,4600)  #hit the pipe
backward(1000,300)
     
        
left(1000,950)     #heading up the ramp
backward(500, 1000)

forward(1400,2000 )# start up the ramp
line_follow_bump(1000)
#KIPR.mav(LMOTOR,1000)
#KIPR.mav(RMOTOR, 1000)
#while KIPR.digital( BUMP_PORT) == 0:
#	pass
#KIPR.ao()
backward(1000,100)
left(1000, 800)
backward(1000, 2000)
        
#=========================================================================================
#									FIRST DIP RUN!!
#=========================================================================================
claw_closed(50)
#line_follow_sensors(800)


line_follow_dist(1000, 6800)
KIPR.ao()
for x in range(2):
	KIPR.mav(LMOTOR, 700)
	KIPR.mav(RMOTOR, 700)
	while KIPR.analog(LINE_PORT_RIGHT) < THRESH:
		pass
	KIPR.ao()
	print ("Over mine!!")
	#IN FRONT OF MINE
	#forward(1000,1550)        
	#over mine
	move_servo_slow( ARM_SERVO, 675, 10)
	claw_fullopen(50)
	move_servo_slow(ELBOW_SERVO, 1650, 10)
	backward(900, 150) #CHANGED

	move_servo_slow( ARM_SERVO, 200, 10)
	move_servo_slow(ELBOW_SERVO, 1300, 10)
	move_servo_slow( ARM_SERVO, 0, 10)
    #in the mine!!

	claw_closed(50)
	claw_fullopen(50)
	claw_closed(25)

    #get out of the mine
	move_servo_slow(ARM_SERVO, 200, 10) #we were at 50, go to 200
	move_servo_slow(ELBOW_SERVO, 1650, 10) #were at 1300

	move_servo_slow(ARM_SERVO, 675, 25)
	right(100,100)
	backward(500, 1000) 
	move_servo_slow(ELBOW_SERVO, 1200, 25)
	backward(500,1000)# drive out of the mine!!
	arm_back(50)
	elbow_down(50)
	left(500,800)
	move_servo_slow(ELBOW_SERVO, 730,25)
	move_servo_slow(ARM_SERVO, 225,25)
	claw_fullopen(50)
	claw_closed(50)
	arm_back(50)
	elbow_down(50)
	KIPR.set_servo_position(ARM_SERVO, 1300)
	KIPR.set_servo_position(ELBOW_SERVO, 2047)
	right(500,500)


line_follow_dist(1000, 6800)
KIPR.ao()
for x in range(1):
	KIPR.mav(LMOTOR, 700)
	KIPR.mav(RMOTOR, 700)
	while KIPR.analog(LINE_PORT_RIGHT) < THRESH:
		pass
	KIPR.ao()
	print ("Over mine!!")
	#IN FRONT OF MINE
	#forward(1000,1550)        
	#over mine
	move_servo_slow( ARM_SERVO, 675, 10)
	claw_fullopen(50)
	move_servo_slow(ELBOW_SERVO, 1650, 10)
	backward(900, 150) #CHANGED
	move_servo_slow( ARM_SERVO, 200, 10)
	move_servo_slow(ELBOW_SERVO, 1300, 10)
	move_servo_slow( ARM_SERVO, 0, 10)
    #in the mine!!

	claw_closed(50)
	claw_fullopen(50)
	claw_closed(25)

    #get out of the mine
	move_servo_slow(ARM_SERVO, 200, 10) #we were at 50, go to 200
	move_servo_slow(ELBOW_SERVO, 1650, 10) #were at 1300

	move_servo_slow(ARM_SERVO, 675, 25)
	right(100,100)
	backward(500, 1000) 
	move_servo_slow(ELBOW_SERVO, 1200, 25)
	backward(500,1000)# drive out of the mine!!
	arm_back(50)
	elbow_down(50)
	left(500,800)
	move_servo_slow(ELBOW_SERVO, 730,25)
	move_servo_slow(ARM_SERVO, 225,25)
	claw_fullopen(50)
	claw_closed(50)
	arm_back(50)
	elbow_down(50)
	KIPR.set_servo_position(ARM_SERVO, 1300)
	KIPR.set_servo_position(ELBOW_SERVO, 2047)
	right(500,500)