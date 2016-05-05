# Pokemon-Style Mini-Game

"""Buttons for three different pokemon, with associated moves
   Random generator that alters the computer pokemon
   display things on the canvas
   Attack library - attacks change as the Exp increases
   Give different pokemon different HP during battle
   Print message when you switch pokemon during a battle
   
"""

# Modules 
import simplegui
import random

#Pokemon Libraries
tallGrass = {"Spearow": ["Peck", "Wing Attack"], 
             "Rattata": ["Scratch", "Bite"], 
             "Weedle": ["Peck", "Poison Dart"]}

pokeBelt = {"Charmander": ["Scratch", "Flamethrower"], 
            "Squirtle": ["Squirt", "Water Gun"], 
            "Bulbasaur": ["Scratch", "Vine Wip"]} 


#Global variables
    # Computer
computer_HP = 100

wild = "Spearow"
attackC1 = ["Peck", 10]
attackC2 = ["Wing Attack", 20]
attackC3 = ["Heal", 15]

    #User
user_HP = 100
user_Exp = 0

pokemon = "Charmander"
attack1 = ["Scratch", 10]
attack2 = ["Flamethrower", 20]
attack3 = ["Heal", 15]


# Helper functions
def new_game():
    """Starts new game, sets and prints game settings"""
    
    global user_HP, computer_HP, text
    user_HP, computer_HP = 100, 100
    
    print
    print
    print "A wild " + wild + " appeared!"
    print "Go " + pokemon + "!" 
    print "What do you do?"
    print

def user_attack(array):
    """An attack array is entered, and the computers HP is decreases, 
       or the users HP increased, according to the attack stats"""
    
    global computer_HP, user_HP
    computer_HP -= array[1]
    
    print pokemon + " used " + array[0] + "!"
    if array[0] == "Heal":
        if user_HP <= (100 - array[1]):	
            user_HP += array[1]
            print pokemon + " regained " + str(array[1]) + " HP!"
        else:
            print "It failed!"
    else:     
        print wild + " lost " + str(array[1]) + " HP."   
    print

def computer_attack(array):
    """An attack array is entered, and the users HP is decreases, 
       or the computers HP increased, according to the attack stats"""
    
    global computer_HP, user_HP
    user_HP -= array[1]
    
    print wild + " used " + array[0] + "!"
    if array[0] == "Heal":
        if computer_HP <= (100 - array[1]):	
            computer_HP += array[1]
            print wild + " regained " + str(array[1]) + " HP!"
        else:
            print "It failed!"
    else:     
        print pokemon + " lost " + str(array[1]) + " HP."   
    print
        
def computer_turn(): 
    """Computer chooses a random attack, and calls the computer_attack function"""
    
    global user_HP, computer_HP
    choice = random.randrange(0, 100)
    
    if 0 <= choice < 40:
        computer_attack(attackC1)

    elif 40 <= choice < 80:
        computer_attack(attackC2)
          
    else:
        computer_attack(attackC3)
    
def gameplay():
    """If the computers HP is zero, restarts the game. If not, 
       the computer attacks. If the users HP is zero, restarts
       the game. If not, waits for the user to choose an attack."""
    
    global user_Exp
    
    if computer_HP <= 0:
        user_Exp += 10
        
        print "The wild " + wild + " fainted!"
        print "You gained 10 Exp!"
        new_game()
    
    else: 
        computer_turn()
        if user_HP <= 0:
            print "Oh no! Your pokemon fainted!"
            new_game()
        else:
            print pokemon + ":", user_HP, "HP"
            print wild + ":", computer_HP, "HP"
            print "What do you do?" 
            print
    
#Event handler functions 
def level1():
    """Calls the level 1 attack"""
    
    user_attack(attack1)
    gameplay()
    
def level2():
    """Calls level 2 attack"""     
    
    user_attack(attack2)
    gameplay()
    
def level3():
    """Calls level 3 attack"""
    
    user_attack(attack3)
    gameplay()

def switchPokeball():
    global pokemon, attack1, attack2
    moves = pokeBelt["Charmander"]
    pokemon = "Charmander"
    attack1[0] = str([moves[0]])
    attack2[0] = str([moves[1]])
      
# creates frame
f = simplegui.create_frame("Pokemon Battle", 200, 200)

# registers event handlers for guess input and range buttons
f.add_button(attack1[0], level1, 100)
f.add_button(attack2[0], level2, 100)
f.add_button(attack3[0], level3, 100)

# starts the frame, starts the game
f.start()
new_game()