# Rock-paper-scissors-lizard-Spock
import random

# helper functions
def name_to_number(name):
    """converts a name to a number"""
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        print "Error: That is not an option." 

def number_to_name(number):
    """converts a number to a name"""
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        print "Error: Number not in range"
    

def rpsls(player_choice): 
    """main game function for rpsls"""
    #prints a blank line separating games
    print 
    #prints out the player's choice
    print "Player chooses " +  player_choice + "."
    #converts the player's choice to player_number
    player_number = name_to_number(player_choice)
    #computes a random guess for comp_number
    comp_number = random.randrange(0, 5)
    #converts comp_number to comp_choice
    comp_choice = number_to_name(comp_number)
    # prints out the computer's choice
    print "Computer chooses " + comp_choice + "."
    # computes the difference of comp_number and player_number modulo five
    difference = (player_number - comp_number) % 5 
    # determines the winner and prints winner message
    if (difference == 1 or difference == 2):
        print "Player wins!"
    elif (difference == 3 or difference == 4):
        print "Computer wins!"
    else: 
        print "Player and computer tie!"
    
# tests the code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



