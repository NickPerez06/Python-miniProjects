'''
This mini project will create the game rock, paper, scissors,
lizard, spock for your enjoyment.
Author: Nicholas Perez
'''

import random

def name_to_number(name):
    '''converts string name to number for rpsls'''

    number = 0

    if( name == "rock" ):
		number = 0
		return number

    elif ( name == "Spock" ):
		number = 1
		return number

    elif ( name == "paper" ):
		number = 2
		return number

    elif ( name == "lizard" ):
		number = 3
		return number

    elif ( name == "scissors" ):
        number = 4
        return number

    else:
        return "This is not one of the choices!"


def number_to_name(number):
    '''Converts number to srting name for rpsls game'''

    if ( number == 0 ):
        return "rock"

    elif ( number == 1 ):
        return "Spock"

    elif ( number == 2 ):
        return "paper"

    elif ( number == 3 ):
        return "lizard"

    elif ( number == 4 ):
        return "scissors"

    else:
        return "Error: you must pick a number between 0-4"


def rpsls(player_choice):
    '''Main Fucntion for rpsls. Will use helper fucntions listed above'''

    print ""
    print "Player chooses " + player_choice
    player_number = name_to_number(player_choice)


    #Below will be the computers choice form 0-4
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses " + comp_choice
    
    #Below will determind who wins or if there is a tie
    result = (player_number - comp_number) % 5
    
    if ( result == 1 or result == 2 ):
        print "Player wins!"

    elif ( result == 3 or result == 4 ):
        print "Computer wins!"

    else:
        print "Player and Computer tie!"


# testing code

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

