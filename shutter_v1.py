import datetime, time
from threading import Timer


def t_INIT = time.time()		# Current time

def t_MAX = time.time()+50		# Time needed by the Shutter to move END to END (second)

def t_UP ="06:50"      # time to move the shutter UP

def t_DOWN ="18:30"		# time to move the shutter DOWN


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

def relayUP_ON():
    GPIO.output(SHUTTER_PIN_UP, 1)                   # relay_UP enabled
    return()
	
def relayUP_OFF():
    GPIO.output(SHUTTER_PIN_UP, 0) 					 # relay_UP disabled	
	print "relay UP turned OFF"
    return()	

def relayDOWN_ON():
    GPIO.output(SHUTTER_PIN_DOWN, 1) 				# relay_DOWN enabled
    return()

def relayDOWN_OFF():
	GPIO.output(SHUTTER_PIN_DOWN, 0) 				# relay_DOWN disabled
	print "relay DOWN turned OFF"
	return()

def relayUP_Status():
	GPIO.input(SHUTTER_PIN_DOWN, 0) 				# relay_DOWN disabled
	return()
	
def relayDOWN_Status
():
	GPIO.output(SHUTTER_PIN_DOWN, 0) 				# relay_DOWN disabled
	return()


def UP():
    while (time.time() <= T_MAX):
       print time.time()           #testing
       print T_MAX					#testing
       print "redony fel"
       time.sleep(1)
	   relayDOWN_OFF()             # relay 1 and relay 2 can't be active in the same time 
	   relayUP_ON()					#shutter is moving UP
	
	relayUP_OFF()					#after T_MAX shutter power has to be turned off
return()

def DOWN():
    while (time.time() <= T_MAX):
       print time.time()			#testing
       print T_MAX					#testing	
       print "redony le" 
       time.sleep(1)
	   relayUP_OFF()             # relay 1 and relay 2 can't be active in the same time 
	   relayDOWN_ON()					#shutter is moving UP
	
	relayDOWN_OFF()					#after T_MAX shutter power has to be turned off   
return()

while (true):
	#time to move shutter UP
	if(datetime.datetime.now().strftime("%H:%M") == t_UP): 		
         UP()
	 continue
	 
	#time to move shutter DOWN
	if(datetime.datetime.now().strftime("%H:%M") == t_DOWN):
		DOWN()
	 continue

	else:
	   print datetime.datetime.now().strftime("%H:%M")
	   time.sleep(15)
	
	