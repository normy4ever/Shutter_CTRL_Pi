import RPi.GPIO as GPIO
import datetime, time
from threading import Timer


t_INIT = time.time()	# Current time

t_SHUTTER_TIME =50

t_MAX = time.time()+t_SHUTTER_TIME	# Time needed by the Shutter to move END to END (second)

t_UP ="23:29"      # time to move the shutter UP

t_DOWN ="23:31"		# time to move the shutter DOWN

# Identify which pin controls the relay for movement UP
SHUTTER_PIN_UP = 17

# Identify which pin controls the relay for movement DOWN
SHUTTER_PIN_DOWN = 18

# relay_UP   --> relay #1
# relay_DOWN   --> relay #2

def GPIOsetup():
    GPIO.setwarnings(False) 
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SHUTTER_PIN_UP, GPIO.OUT)
    GPIO.setup(SHUTTER_PIN_DOWN, GPIO.OUT)
    GPIO.output(SHUTTER_PIN_UP, 1)			# relay works with inverse logic 0=OFF ; 1=ON
    GPIO.output(SHUTTER_PIN_DOWN, 1)			# relay works with inverse logic 0=OFF ; 1=ON

def relayUP_ON():
    GPIO.output(SHUTTER_PIN_UP, 0)                   # relay_UP enabled
    return()
	
def relayUP_OFF():
    GPIO.output(SHUTTER_PIN_UP, 1) 					 # relay_UP disabled	
    print "relay UP turned OFF"
    return()	

def relayDOWN_ON():
    GPIO.output(SHUTTER_PIN_DOWN, 0) 				# relay_DOWN enabled
    return()

def relayDOWN_OFF():
	GPIO.output(SHUTTER_PIN_DOWN, 1) 				# relay_DOWN disabled
	print "relay DOWN turned OFF"
	return()

def relayUP_Status():
	GPIO.input(SHUTTER_PIN_DOWN, 32) 				# relay_DOWN disabled
	return()
	
def relayDOWN_Status():
	GPIO.output(SHUTTER_PIN_DOWN, 33) 				# relay_DOWN disabled
	return()


def UP():
#    while (time.time() <= t_MAX):
       print time.time()           #testing
       print t_MAX					#testing
       print "redony fel"
       time.sleep(1)
       relayDOWN_OFF()             # relay 1 and relay 2 can't be active in the same time 
       relayUP_ON()
       time.sleep(t_SHUTTER_TIME - 1) 	#shutter is moving UP
       relayUP_OFF()					#after T_MAX shutter power has to be turned off
       return()

def DOWN():
#    while (time.time() <= t_MAX):
       print time.time()			#testing
       print t_MAX					#testing	
       print "redony le" 
       time.sleep(1)
       relayUP_OFF()             # relay 1 and relay 2 can't be active in the same time 
       relayDOWN_ON()					#shutter is moving UP
       time.sleep(t_SHUTTER_TIME - 1)       
       relayDOWN_OFF()					#after T_MAX shutter power has to be turned off   
       return()


GPIOsetup()

while (datetime.datetime.now()):
	#time to move shutter UP
#	print datetime.datetime.now().strftime("%H:%M")
#	print t_UP
#	time.sleep(25)
	if(datetime.datetime.now().strftime("%H:%M") == t_UP): 		
        	UP()
		#continue
	 
	#time to move shutter DOWN
	if(datetime.datetime.now().strftime("%H:%M") == t_DOWN):
		DOWN()
		#continue
	try:
		print datetime.datetime.now().strftime("%H:%M")
		time.sleep(15)
	except KeyboardInterrupt:
		GPIO.output(SHUTTER_PIN_UP, 1)                      # relay works with inverse logic 0=OFF ; 1=ON
    		GPIO.output(SHUTTER_PIN_DOWN, 1)                    # relay works with inverse logic 0=OFF ; 1=ON  
    		GPIO.cleanup()
		break
print "Good bye!"
