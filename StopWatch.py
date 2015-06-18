# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 21:41:06 2015

@author: ali
"""

import simplegui
#import random
 
# global variables
time = 0
attempts = 0
wins = 0
started = False

def format(h):
    a = (h / 600)
    b = ((h // 100) % 6)
    c =  ((h // 10) % 10)
    d =  (h % 10)
    clock = str(a) +  ":" + str(b) + "" + str(c) + "." + str(d)
    return clock
    clock = str(a) +  ":" + str(b) + "" + str(c) + "." + str(d)
    return clock

# define event handlers for buttons; "Start", "Stop", "Reset"
def start_timer():
    global started
    timer.start()
    started = True
     
def stop_timer():
    timer.stop();
    global time, wins, attempts, started
    if time % 10 == 0:
        if started:
            wins = wins + 1
            not started 
    attempts = attempts + 1
        
def reset_timer():
    global time, started, attempts, wins
    timer.stop()
    time = 0
    wins = 0
    attempts = 0
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1
    
# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(time), (120,120), 50, "Red")
    canvas.draw_text("Wins|Attemps: " + str(wins) + "|" + str(attempts), (200,30), 20, "Green")
         
# create frame
f = simplegui.create_frame("StopWatch Game", 400, 200)
 
# register event handlers
f.add_button("Start", start_timer, 100);
f.add_button("Stop", stop_timer, 100);
f.add_button("Reset", reset_timer, 100);
timer = simplegui.create_timer(100, timer_handler)
f.set_draw_handler(draw_handler)
 
# start frame
f.start()