"""
Cookie Clicker Simulator
"""

import simpleplot
#import user40_31KnFXN6dW_5 as test
import math 

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self.__total_cookies__ = 0.0 
        self.__current_cookies__ = 0.0 
        self.__current_time__ = 0.0 
        self.__current_cps__ = 1.0 
        self.__history__ = [(0.0, 1.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        return str(self.__history__[-1]) 
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        """
        return float(self.__current_cookies__) 
    
    def get_cps(self):
        """
        Get current CPS
        """
        return float(self.__current_cps__)
    
    def get_time(self):
        """
        Get current time
        """
        return float(self.__current_time__) 
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]
        """
        return list(self.__history__) 

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if cookies > self.__current_cookies__: 	
            return float(math.ceil((cookies - (self.__current_cookies__)) / self.__current_cps__)) 
        else:
            return 0.0 
           
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time > 0:
            self.__current_time__ += time
            self.__total_cookies__ += time * self.__current_cps__
            self.__current_cookies__ += time * self.__current_cps__
 
       
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if self.__current_cookies__ >= cost: 
            self.__current_cookies__ -= cost
            self.__current_cps__ += additional_cps
            self.__history__.append((self.__current_time__, 
                                     item_name, cost, self.__total_cookies__)) 
 
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """

    new_build_info = build_info.clone()
    new_state= ClickerState()
    
    while new_state.get_time() <= duration: 
        if new_state.get_time() > duration: 
            break
        
        item_type = strategy(new_state.get_cookies(), 
                             new_state.get_cps(), 
                             new_state.get_history(), 
                             (duration - new_state.get_time()), new_build_info)  
       
        if item_type == None:
            break
        
        cost = new_build_info.get_cost(item_type)
        additional_cps = new_build_info.get_cps(item_type) 
        wait_time = new_state.time_until(cost)
        
        if (new_state.get_time() + wait_time) > duration: 
            break 
        else:  
            new_state.wait(wait_time) 
            new_state.buy_item(item_type, cost, additional_cps)
            new_build_info.update_item(item_type)
    
    
    new_state.wait((duration - new_state.get_time())) 
    return new_state 
      
def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    item_list = list(build_info.build_items())
    cheapest = None
    funds = cookies + (time_left * cps) 
    for item in item_list: 
        cost = build_info.get_cost(item)
        if (cheapest == None): 
            if (cost <= funds): 
                cheapest = item
        elif (cost <= build_info.get_cost(cheapest)) and (cost <= funds):
            cheapest = item
    
    return cheapest  

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    item_list = list(build_info.build_items())
    expensive = None        
    funds = cookies + (time_left * cps)  
    
    for item in item_list:  
        cost = build_info.get_cost(item)
        if (expensive == None):
            if (cost <= funds): 
                expensive = item
        elif (cost >= build_info.get_cost(expensive)) and (cost <= funds): 
            expensive = item
    return expensive  

def strategy_cps(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    item_list = list(build_info.build_items())
    high_cps = None        
    funds = cookies + (time_left * cps)  
    
    for item in item_list:  
        cost = build_info.get_cost(item)
        item_cps = build_info.get_cps(item) 
        if (high_cps == None):
            if (cost <= funds): 
                high_cps = item
        elif (item_cps >= build_info.get_cps(high_cps)) and (cost <= funds): 
            high_cps = item
    return high_cps 

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    if (cps < 5000000) or (cookies < 72000000): 
        return strategy_cheap(cookies, cps, history, time_left, build_info) 
    else: 
        return strategy_cps(cookies, cps, history, time_left, build_info) 

def strategy_best2(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    if cookies < 72000000: 
        return strategy_cheap(cookies, cps, history, time_left, build_info) 
    elif cookies < 100000000: 
        return strategy_cps(cookies, cps, history, time_left, build_info) 
    else: 
        return strategy_cheap(cookies, cps, history, time_left, build_info) 

def run_strategy(strategy_name, strategy_name2, time, strategy, strategy2):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state
    state2 = simulate_clicker(provided.BuildInfo(), time, strategy2)
    print strategy_name2, ":", state2 

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    history = state.get_history()
    history = [(item[0], item[3]) for item in history]

    history2 = state2.get_history() 
    history2 = [(item[0], item[3]) for item in history2]

    simpleplot.plot_lines(strategy_name, 700, 500, 'Time', 'Total Cookies', [history, history2], True, [strategy_name, strategy_name2])

def run():
    """
    Run the simulator.
    """    
    #run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)
    #run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)
    #run_strategy("Cursor", SIM_TIME, strategy_none)
    
    # Add calls to run_strategy to run additional strategies
    #run_strategy("Cheap", 1000, strategy_cheap)
    #run_strategy("Expensive", 1000, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)
#run()
#my_object = ClickerState()
#test.run_suite(my_object)
print "Best_", simulate_clicker(provided.BuildInfo(), SIM_TIME, strategy_best)

print "Best2", simulate_clicker(provided.BuildInfo(), SIM_TIME, strategy_best2)

#run_strategy("Best1", "Best2", 100000, strategy_best, strategy_best2)
