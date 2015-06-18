'''
This is a template for "Guess the number" mini-project
input will come from buttons and an input field
all output for the game will be printed in the console
Author: Nicholas Perez
'''

import simplegui
import random

#global variables
num_range = 100
secret_num = 0
num_guess = 0

def new_game():
    '''
    helper function to start and restart the game
    '''
    global num_range
    global secret_num
    global num_guess
    
    secret_num = random.randrange(0, num_range)
    
    if ( num_range == 100 ):
        num_guess = 7
    elif ( num_range == 1000 ):
        num_guess = 10
    
    print""
    print "New game. Range is from 0 to", num_range
    print "Number of guesses remaining is", num_guess


    # define event handlers for control panel
def range100():
    '''
    button that changes the range to [0,100) and starts a new game 
    '''
    
    global num_range
    num_range = 100
    new_game()   
    

def range1000():
    '''
    button that changes the range to [0,1000) and 
    starts a new game     
    '''
    
    global num_range 
    num_range = 1000
    new_game()
    
def input_guess(guess):
    '''
    Function to take input from user and check to see is guess
    is correct or not
    '''
    
    global secret_num
    global num_guess
    
    print ""
    print "Guess was " + guess
    num_guess -= 1
    print "Number of remaning guesses is", num_guess
    
    if ( int(guess) == secret_num ):
        print "Correct!"
        new_game()
        return
    
    elif ( int(guess) > secret_num ):
        answer = "Lower!"
    
    else:
        answer = "Higher!"
        
        
        
    if ( num_guess == 0 ):
        print "You ran out of guesses. The number was", secret_num
        new_game()
        return
    else:
        print answer

# create frame
frame = simplegui.create_frame('Guess the number', 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)	
frame.add_input("Enter guess", input_guess, 200)

# call new_game 
new_game()

frame.start()
# always remember to check your completed program against the grading rubric
