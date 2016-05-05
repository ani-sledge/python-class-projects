# "Guess the number" Mini-Project

"""In this game, the user must guess a secret random number.
   The user can select a range of 0-100 or 0-1000 using buttons, and input their
   guesses into an input field. If the range is 100, the user has 7 chances to 
   guess. If the range is 1000, the user has 10 chances. The game prints whether 
   the guess was too high, too low, or correct. If the user wins or runs out of 
   chances, the game restarts. 
"""

# Modules 
import simplegui
import random
import math

# Global variables
current_range = 100
chances_left = 7 

# Helper functions
def new_game():
    """Chooses a secret random number, sets # of chances, and prints game settings"""
    
    global secret_number, current_range, chances_left
    secret_number = random.randrange(0, current_range)
    chances_left = int(math.ceil(math.log((current_range + 1), 2)))
    
    print
    print "NEW GAME"
    print "Range: 0 -", current_range
    print "You have " + str(chances_left) + " chances to guess." 
    print 

def decrement():
    """reduces the number of chances left by one, and prints the number.
       If the user has run out of chances, it restarts the game."""
    
    global chances_left
    chances_left -= 1
    
    if chances_left > 0: 	
        print "Chances left:", chances_left
        print
    else:
        print "Sorry, you've run out of guesses!"
        print "The correct number was " + str(secret_number) + "."
        new_game()
    
# Event handler functions
def range100():
    """updates the range to [0, 100) and guess limit to 7"""
    
    global current_range
    current_range = 100
    new_game()

def range1000():
    """updates the range to [0, 1000) and guess limit to 10"""     
    
    global current_range
    current_range = 1000
    new_game() 
    
def input_guess(guess):
    """Compares the user guess to the secret_number, and tells
       the user whether their guess was higher, lower or correct."""
    
    print "Your guess was " + guess + "."
    
    guess_number = int(guess)
        
    if guess_number > secret_number:
        print "Your guess is too high!"
        decrement()
    elif guess_number < secret_number:
        print "Your guess is too low!"
        decrement()
    elif guess_number == secret_number:
        print "Correct!"
        new_game()
    else: 
        print "Error: input_guess"
    
          
    
# creates frame
f = simplegui.create_frame("Guess the Number", 200, 200)

# registers event handlers for guess input and range buttons
f.add_input('Enter your guess:', input_guess, 100)
f.add_button('Range: 0-100 ', range100, 100)
f.add_button('Range: 0-1000', range1000, 100)


# starts the frame, prints welcome, starts the game
f.start()
print "Welcome to Guess the Number!"
print
new_game()