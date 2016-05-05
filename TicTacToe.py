"""
Monte Carlo Tic-Tac-Toe Player
"""
import random
import poc_ttt_gui
import poc_ttt_provided as provided
import user40_hxL7GIqHy0_11 as test

# Constants for Monte Carlo simulator
NTRIALS = 15         # Number of trials to run
SCORE_CURRENT = 1.5 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

# Helper functions

def mc_trial(board, player):
    """
    Plays a trial game of tic-tac-toes with random moves.
    """
    current_player = player 
    empty_cells = board.get_empty_squares()
    while board.check_win() == None: 
        position = random.choice(empty_cells)
        board.move(position[0], position[1], current_player)
        empty_cells.remove(position)
        current_player = provided.switch_player(current_player) 


def mc_update_scores(scores, board, player):
    """
    Updates the scores grid according to the completed game board.
    """
    x_score = 0 #2
    o_score = 0 #3 
    board_state = board.check_win()
    
    if board_state == provided.PLAYERX or board_state == provided.PLAYERO: 
        if player == provided.PLAYERX:
            if board_state == provided.PLAYERX: 
                x_score = SCORE_CURRENT
                o_score = -SCORE_OTHER
            
            elif board_state == provided.PLAYERO: 
                x_score = -SCORE_CURRENT
                o_score = SCORE_OTHER
            
        elif player == provided.PLAYERO:
            if board_state == provided.PLAYERO: 
                o_score = SCORE_CURRENT
                x_score = -SCORE_OTHER
            
            elif board_state == provided.PLAYERX: 
                o_score = -SCORE_CURRENT
                x_score = SCORE_OTHER
    
        dimension = board.get_dim() 
        for row in range(dimension):
            for col in range(dimension): 
                current_square = board.square(row, col)
            
                if current_square == provided.PLAYERX:
                    scores[row][col] += x_score
                elif current_square == provided.PLAYERO:
                    scores[row][col] += o_score
                elif current_square == provided.EMPTY:
                    scores[row][col] += 0 


def get_best_move(board, scores):  
    """
    Finds all empty cells with the maximum score and returns one randomely.
    """
    empty_squares = board.get_empty_squares()
    empty_scores = [] 
    for index in empty_squares: 
        empty_scores.append(scores[index[0]][index[1]]) 
    
    maximum = max(empty_scores)  

    winners = [] 
    
    for index in empty_squares: 
            if scores[index[0]][index[1]] == maximum:  
                winners.append(index)
    
    if len(winners) > 0: 
        return random.choice(winners)


def mc_move(board, player, trials):
    """
    Chooses a move for the machine player using a MC simulation.
    """
    dimension = board.get_dim() 
    scores = [[0 for dummy_col in range(dimension)] 
              for dummy_row in range(dimension)]
    
    for dummy_trial in range(trials): 
        trial_board = board.clone()   	              #copy the board
        mc_trial(trial_board, player) 	              #run a trial
        mc_update_scores(scores, trial_board, player) #score the trial
    return get_best_move(board, scores) 			  
    

#test.run_suite(mc_move, NTRIALS)

#provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
