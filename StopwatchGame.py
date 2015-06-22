'''
This is a project for "Stopwatch: The Game"
Author: Nicholas Perez
Date: 6/19/2015
'''

import simplegui

# define global variables
time = 0
correct_stops = 0
total_stops = 0
stop = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    '''
    function that converts time to string format,
    A:BC.D
    '''
    A = t // 600 				#Minutes
    B = ( t // 10) % 60 // 10	#tens of seconds
    C = (t // 10) % 10			#the amount of seconds in excess of tens of seconds
    D = t % 10					#remaining tenths of seconds
    
    return str(A)+":"+str(B)+str(C)+"."+str(D)
        
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    '''
    function that starts timer
    '''
    global stop
    stop = False
    timer.start()
    
def Stop():
    '''
    funciton that stops timer
    '''
    global stop, correct_stops, total_stops
    stop = True
    
    if( time % 10 == 0 and time != 0 ):
        correct_stops += 1
        total_stops += 1
        
    elif ( time != 0 ):
        total_stops += 1
    
    timer.stop()
    
def Reset():
    ''' 
    function that changes global variables to 0
    '''
    timer.stop()
    global time, stop, correct_stops, total_stops
    correct_stops = 0 
    total_stops = 0
    stop = True
    time = 0

# define event handler for timer with 0.1 sec interval
def create_timer():
    global time
    time += 1
    

# define draw handler
def draw(canvas):
    canvas.draw_text(str(format(time)), (150, 200) , 45, "white")
    canvas.draw_text((str(correct_stops) + "/" + str(total_stops)), (350, 25), 25, "white")
    
# create frame and timer
frame = simplegui.create_frame("Stopwatch: The game", 400, 300)
timer = simplegui.create_timer(100, create_timer)

# register event handlers
frame.add_button("Start", Start)
frame.add_button("Stop", Stop)
frame.add_button("Reset", Reset)
frame.set_draw_handler(draw)


# start frame
frame.start()
