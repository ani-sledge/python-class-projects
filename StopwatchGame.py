# "Stopwatch: The Game"

"""This game displays a stop watch, which can be controlled 
   by the start, stop, and reset buttons. The users score (the 
   number of times the user has stopped the watch on a whole 
   second (2.0, ect.), over the number of total stops) is 
   displayed in the upper right hand corner. The reset button 
   sets the timer and the users score back to zero."""


# Modules
import simplegui

# Global variables
counter = 0
total_stops = 0
successful_stops = 0
timer_running = False



# Helper functions
def format(t):
    """Takes a number and returns a string in the format 
    'A:BC.D'."""
    
    D = t % 10
    A = (t // 10) // 60 
    B = ((t // 10) % 60) / 10
    C = ((t // 10) % 60) % 10
    return (str(A) + ":" + str(B) + str(C) + "." + str(D))

def score():
    """Increments total_stops. If the timer was stopped on a
       whole second, increments successful stops."""
    
    global successful_stops, total_stops, counter
    total_stops += 1  
    if counter % 10 == 0:
        successful_stops += 1
    
# Event handlers
def start():
    """Starts the timer; sets boolian to indicate that the timer
      is on."""
    
    global timer_running
    timer_running = True
    timer.start()
    
def stop():
    """Stops the timer; calls the score function if the timer 
       was running when the stop button was clicked; sets boolian
       to indicate that the timer is off."""
    
    global timer_running
    timer.stop()
    if timer_running:	
        score()
    timer_running = False
    
def reset():
    """Stops the timer; resets the timer and score to zero.
       Sets boolian to indicate that the timer is off."""
    
    timer.stop()
    global counter, timer_running, successful_stops, total_stops
    counter, successful_stops, total_stops = 0, 0, 0
    timer_running = False

# Timer handler
def tick():
    """Increments the tenths of a second counter."""
    
    global counter
    counter += 1

# Draw handler
def draw(canvas):
    """Draws the time and users score to the canvas"""
    
    canvas.draw_text(str(format(counter)), (60, 110), 32, "White")
    canvas.draw_text((str(successful_stops) + "/" + str(total_stops)), 
                     (150, 40), 20, "White")
    
    
    
# Creates frame
frame = simplegui.create_frame("Stopwatch: The Game", 200, 200)

# Registers event handlers
timer = simplegui.create_timer(100, tick)
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)
frame.set_draw_handler(draw)

#Starts frame
frame.start()
