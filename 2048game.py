"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    result = [0] * len(line)
    store = []
    num = 0
    for index in range(len(line)):
        if line[index] != 0:
            if index != 0 and (num > 0) and (line[index] == result[num - 1]) and (num - 1) not in store:
                result[num - 1] = line[index]*2 
                store.append(num-1)
            else:
                result[num] = line[index] 
                num += 1            
    return result

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._grid_height_ = grid_height
        self._grid_width_ = grid_width 
        self.reset()
        
        self._indices_ = {UP: [],
                        DOWN: [],
                        LEFT: [],
                        RIGHT: []
                       }
        for col in range(self._grid_width_): 
            self._indices_[UP].append((0, col))
            self._indices_[DOWN].append((self._grid_height_ - 1, col))
        for row in range(self._grid_height_):
            self._indices_[LEFT].append((row, 0))
            self._indices_[RIGHT].append((row, self._grid_width_ - 1))
        
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._cells_ = [[0 for dummy_col in range(self._grid_width_)] 
                             for dummy_row in range(self._grid_height_)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        class_string = ""
        for row in self._cells_:
            class_string += str(row) + "\n"
             
        return class_string

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height_

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width_

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        changed_flag = False
        
        if direction == UP or direction == DOWN: 
            num_steps = self._grid_height_
        elif direction == LEFT or direction == RIGHT:
            num_steps = self._grid_width_ 
        
        print num_steps             
        for tile in self._indices_[direction]:
            temp_list = []
            for step in range(num_steps):       
                row = tile[0] + step * OFFSETS[direction][0]
                col = tile[1] + step * OFFSETS[direction][1]
                thing = self._cells_[row][col]
                temp_list.append(thing)
            new_list = merge(temp_list)
            
            ind = 0
            for step in range(num_steps):
                row = tile[0] + step * OFFSETS[direction][0]
                col = tile[1] + step * OFFSETS[direction][1]
                
                if self._cells_[row][col] != new_list[ind]:
                    changed_flag = True
                
                self._cells_[row][col] = new_list[ind] 
                ind += 1
        
        if changed_flag:
            self.new_tile()

            
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        open_tiles = []
        for row in range(self._grid_height_):
            for col in range(self._grid_width_):
                if self._cells_[row][col] == 0:
                    open_tiles.append((row, col))
        tile = open_tiles[random.randrange(len(open_tiles))]
        if random.randrange(0, 10) == 0:
            self._cells_[tile[0]][tile[1]] = 4
        else:
            self._cells_[tile[0]][tile[1]] = 2        
       
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._cells_[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._cells_[row][col]

poc_2048_gui.run_gui(TwentyFortyEight(4, 4))



