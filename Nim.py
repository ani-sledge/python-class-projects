"""
A simple Monte Carlo solver for Nim
http://en.wikipedia.org/wiki/Nim#The_21_game
"""

import random
import codeskulptor
codeskulptor.set_timeout(20)

MAX_REMOVE = 3
TRIALS = 10000

def evaluate_position(num_items):
    """
    Monte Carlo evalation method for Nim
    """
    move_wins = [0 for num in range(MAX_REMOVE)] 
    winners = []
    
    for move in range(1, (MAX_REMOVE + 1)):
        wins = 0 

        for trial in range(TRIALS): 
            initial_num = int(num_items) - move 
            turn = 1
            
            while initial_num > 0: 
                initial_num -= random.randrange(1, 4)
                turn += 1 
            
            if turn % 2 != 0:
                wins += 1

        move_wins[move - 1] = wins 
    
    maximum = max(move_wins)
 
    for index in range(len(move_wins)): 
        if move_wins[index] == maximum: 
            winners.append(index + 1)

    return random.choice(winners) 

def play_game(start_items):
    """
    Play game of Nim against Monte Carlo bot
    """
    
    current_items = start_items
    print "Starting game with value", current_items
    while True:
        comp_move = evaluate_position(current_items)
        current_items -= comp_move
        print "Computer choose", comp_move, ", current value is", current_items
        if current_items <= 0:
            print "Computer wins"
            break
        player_move = int(input("Enter your current move"))
        current_items -= player_move
        print "Player choose", player_move, ", current value is", current_items
        if current_items <= 0:
            print "Player wins"
            break

play_game(10)


                 
    