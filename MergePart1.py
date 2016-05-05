"""
Merge function for 2048 game.
"""

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
 
print merge([2, 0, 2, 4]), "Result: [4, 4, 0, 0]"
print merge([0, 0, 2, 2]), "Result: [4, 0, 0, 0]"
print merge([2, 2, 0, 0]), "Result: [4, 0, 0, 0]"
print merge([2, 2, 2, 2, 2]), "Result: [4, 4, 2, 0, 0]"
print merge([8, 16, 16, 8]), "Result: [8, 32, 8, 0]"
print merge([4, 4, 0, 8, 2]), "Result: [8, 8, 2, 0, 0]"

