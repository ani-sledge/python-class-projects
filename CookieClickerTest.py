"""
Test suite for Cookie Clicker Simulator 
"""

import poc_simpletest

def run_suite(click_object):
    """
    Some informal testing code
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite() 
    
    # test format_function on various inputs
    suite.run_test(str(click_object), "(0.0, None, 0.0, 0.0)", "Test #1:")
    suite.run_test(click_object.get_cookies(), 0.0, "Test #2:")
    suite.run_test(click_object.get_cps(), 1.0, "Test #3:")
    suite.run_test(click_object.get_time(), 0.0, "Test #4:")
    suite.run_test(click_object.get_history(), [(0.0, None, 0.0, 0.0)], "Test #5:")
    suite.run_test(click_object.time_until(100), 100.0, "Test #6:") 
    suite.run_test(click_object.wait(100), None, "Test #7:") 
    suite.run_test(click_object.get_cookies(), 100.0, "Test #8:") 
    suite.run_test(click_object.get_cps(), 1.0, "Test #8:") 
    suite.run_test(click_object.get_time(), 100.0, "Test #8:") 
    suite.run_test(click_object.get_history(), [(0.0, None, 0.0, 0.0)], "Test #9:") 
    suite.run_test(click_object.buy_item("item", 50, 1), None, "Test #10:")
    suite.run_test(click_object.get_cookies(), 50.0, "Test #11:") 
    suite.run_test(click_object.get_cps(), 2.0, "Test #12:") 
    suite.run_test(click_object.get_time(), 100.0, "Test #13:") 
    suite.run_test(click_object.get_history(), [(0.0, None, 0.0, 0.0), 
                                                (100.0, "item", 50.0, 100.0)], "Test #14:")
    
    suite.run_test(click_object.wait(100), None, "Test #15:") 
    suite.run_test(click_object.wait(0), None, "Test #16:")
    suite.run_test(click_object.time_until(450), 100.0, "Test #17:")
    suite.run_test(click_object.get_cookies(), 250.0, "Test #18:")  
    suite.run_test(click_object.get_time(), 200.0, "Test #18:")  
    suite.run_test(click_object.buy_item("item", 50, 1), None, "Test #19:")
    suite.run_test(click_object.buy_item("item", 5000000, 1), None, "Test #19:")
    suite.run_test(click_object.get_cookies(), 200.0, "Test #20:") 
    suite.run_test(click_object.get_cps(), 3.0, "Test #21:") 
    suite.run_test(click_object.get_time(), 200.0, "Test #22:") 
    suite.run_test(click_object.get_history(), [(0.0, None, 0.0, 0.0), 
                                                (100.0, "item", 50.0, 100.0), 
                                                (200.0, "item", 50.0, 300.0)], "Test #23:")
    
    
    print click_object.get_history() 
    suite.report_results() 

