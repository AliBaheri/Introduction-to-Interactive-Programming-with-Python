# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
new_range = 100
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    #if input_guese() == random.randrange(): return correct 
    # remove this when you add your code    
    secret_number = random.randrange(0, num_range)
    if new_range = 100:
        num_remaining_guesses = 7
    elif new_range = 1000
        num_remaining_guesses = 10


# define event handlers for control panel
def range100():
    #button that changes the range to [0,100) and starts a new game 
    print random.randrange(0, 100)
    # remove this when you add your code    
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    print random.randrange(0, 1000)
    new_game()
    
def input_guess(guess):
    # main game logic goes here
       num_remaining_guesses -= 1
        #convert the input to an int
       guess_number = int(guess)	
    global num_remaining_guesses, secret_number
    if guess_number == secret_number:
            print "Correct!"
            init_game()
        else:
            if guess_number < secret_number:
                print "Higher!"
            elif guess_number > secret_number:
                print "Lower!"
        
            if num_remaining_guesses == 0:
                print "You lost the game!"
                print ""
                init_game() 
    pass

    
# create frame

f = simplegui.create_frame("Guess the number",200,200)


# register event handlers for control elements and start frame
f.add_button (" Range is [0,100)",range100,200)
f.add_button (" Range is [0,1000)",range1000,200)
f.add_button (" Enter a guess number ",get_input, 200)

# call new_game 
new_game()
