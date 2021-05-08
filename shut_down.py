#!/usr/bin/python
import os, sys
import ctypes
import time

KIPR=ctypes.CDLL("/usr/lib/libkipr.so")
    
def shut_down():
	print("starting shut_down_in")
	#start_time = time.time()
	#while time.time() - start_time < end_time:
		#pass
	time.sleep(118)

	print("exiting")
	KIPR.ao()
	KIPR.create_disconnect()
	sys.exit()
        
	