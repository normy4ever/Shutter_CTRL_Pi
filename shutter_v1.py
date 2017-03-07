import datetime, time
from threading import Timer

def hello():
    print "hello, world"
#    t = Timer(3,hello)
#    t.start()

def UP():
    a = time.time()
    b = time.time()+50
    while (time.time() <= b):
       print time.time()
       print b
       print "redony fel"
       time.sleep(1)
    return()

def DOWN():
    print "redony le"

	
t_UP = Timer(50, UP)

t_DOWN = Timer(50, DOWN)

#t.start() # after 3 seconds, "hello, world" will be printed

# timer will wake up ever 3 seconds, while we do something else
#d_date = datetime.datetime.now()
#d_time = d_date.strftime("%H:%M")
while (datetime.datetime.now()):
	if(datetime.datetime.now().strftime("%H:%M") == "22:39"):
         UP()
	 continue
#	 print datetime.datetime.now().strftime("%H:%M")
	else:
	   print datetime.datetime.now().strftime("%H:%M")
#	   print time.time()
#	   print time.time()+50
	   time.sleep(15)

