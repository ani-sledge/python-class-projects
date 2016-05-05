"""
Test suite for tic tac toe"
"""

import poc_simpletest
import random
import poc_ttt_provided as provided

def run_suite(mc_move, trials):
    """
    Test to see if mc_move consistently produces the best next move. 
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # run_test(self, computed, expected, message = "")
    # test mc_move on various inputs
    for dummy_num in range(5): 
        suite.run_test(mc_move(provided.TTTBoard(3, False, 
                                                [[provided.PLAYERX, provided.EMPTY, provided.EMPTY], 
                                                 [provided.PLAYERO, provided.PLAYERO, provided.EMPTY], 
                                                 [provided.EMPTY, provided.PLAYERX, provided.EMPTY]]), 
                               provided.PLAYERO, trials), (1, 2), "Test #1:")
    for dummy_num in range(5): 
        suite.run_test(mc_move(provided.TTTBoard(3, False, 
                                                [[provided.PLAYERX, provided.EMPTY, provided.EMPTY], 
                                                 [provided.EMPTY, provided.PLAYERO, provided.PLAYERO], 
                                                 [provided.EMPTY, provided.EMPTY, provided.PLAYERX]]), 
                               provided.PLAYERX, trials), (1, 0), "Test #2:")
    for dummy_num in range(5): 
        suite.run_test(mc_move(provided.TTTBoard(3, False, 
                                                [[provided.PLAYERX, provided.PLAYERO, provided.EMPTY], 
                                                 [provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], 
                                                 [provided.EMPTY, provided.PLAYERO, provided.EMPTY]]), 
                               provided.PLAYERO, trials), (2, 2), "Test #3:")
    
    
    suite.report_results()
    
    
    
