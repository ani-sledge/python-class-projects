# Rock-paper-scissors-lizard-Spock
"""This game uses buttons to create a user choice 
   (Rock, paper, scissors, lizard, or Spock) and 
   compares that to a randomly generated computer choice.
   
   The winner is assigned as follows:
   Rock beats scissors and lizard.
   Scissors beats paper and lizard. 
   Paper beats rock and Spock.
   Lizard beats paper and Spock. 
   Spock beats rock and scissors.""" 

import random
import simplegui

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
    
    #prints out the player's choice
    print 
    print "Player chooses " +  player_choice + "."
    
    #converts the player's choice to player_number
    player_number = name_to_number(player_choice)
    
    if ( 0 <= player_number <= 4):
        #produces random guess for comp_number
        comp_number = random.randrange(0, 5)
        comp_choice = number_to_name(comp_number)
        print "Computer chooses " + comp_choice + "."
    
        # determines the winner 
        difference = (player_number - comp_number) % 5 
        if (difference == 1 or difference == 2):
            print "Player wins!"
        elif (difference == 3 or difference == 4):
            print "Computer wins!"
        else: 
            print "Player and computer tie!"
    else:
        pass
    
#event handlers
def choose_rock():
    return rpsls("rock")

def choose_paper():
    return rpsls("paper")

def choose_scissors():
    return rpsls("scissors")

def choose_lizard():
    return rpsls("lizard")

def choose_spock():
    return rpsls("Spock")
        
#create frame
f = simplegui.create_frame("RPSLS", 300, 300)

#assign event handlers
f.add_button("Rock", choose_rock, 100)
f.add_button("Paper", choose_paper, 100)
f.add_button("Scissors", choose_scissors, 100)
f.add_button("Lizard", choose_lizard, 100)
f.add_button("Spock", choose_spock, 100)

#start frame
f.start() 
