"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move
"""




class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """
    
    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self._board_ = [0]
    
    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are numbered in ascending order from right to left
        """
        self._board_ = list(configuration) 
    
    def __str__(self):
        """
        Return string representation for Mancala board
        """
        board = list(self._board_)
        board.reverse()
        return str(board)
    
    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        return self._board_[house_num]

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        for house in range(1, len(self._board_)):
            if self._board_[house] > 0:
                return False
        else:
            return True
    
    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        if house_num == self._board_[house_num] and house_num != 0:
            return True
        else:
            return False
    
    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        if self.is_legal_move(house_num):  
            self._board_[house_num] = 0
            for num in range(house_num):
                self._board_[num] += 1

    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        for house in range(len(self._board_)):
            if self.is_legal_move(house):
                return house
        return 0
        #something may be wrong here
    
    def plan_moves(self):
        """
        Returns a sequence (list) of legal moves based on the following heuristic: 
        After each move, move the seeds in the house closest to the store 
        when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """
        moves_list = []
        current_house = self.choose_move()
        while current_house != 0:
            moves_list.append(current_house)
            self.apply_move(current_house)
            current_house = self.choose_move()
        return moves_list
           
 

# Create tests to check the correctness of your code

def test_mancala():
    """
    Test code for Solitaire Mancala
    """
    
    my_game = SolitaireMancala()
    print "Testing init - Computed:", my_game, "Expected: [0]"
    
    config1 = [0, 0, 1, 1, 3, 5, 0]    
    my_game.set_board(config1)   
    print "Testing set_board - Computed:", str(my_game), "Expected:", str([0, 5, 3, 1, 1, 0, 0])
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(1), "Expected:", config1[1]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(2), "Expected:", config1[2]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(3), "Expected:", config1[3]
    print "First move choice:", my_game.choose_move(), ": Expected: 5"
    print my_game.plan_moves()
    
test_mancala()


# Import GUI code once you feel your code is correct
# import poc_mancala_gui
# poc_mancala_gui.run_gui(SolitaireMancala())
