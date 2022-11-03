# Noah Hanshaw
# 11/27/2020
# D&D Patrick's Stat Rolling Code

# Import the random number and numerical python
import random as r
import numpy as np

def StatRoller():                           # Function for the Stat Roller
    b = []                                  # Create an empty vector for final rolled values
    for i in range(6):                      # Begin the loop for the 6 stat numbers
        y = []                              # Create an empty vector for generated values
        for i in range(4):                  # Begin the loop for 4 individual numbers 
            x = (r.randrange(1,7))          # Generate a random integer between 1 & 6
            if x == 1:                      # If the integer = 1, replace it with a seperate random integer between 2 & 6
                x = r.randrange(2,7)
            y.append(x)                     # Add the integer to the vector y
        y.remove(min(y))                    # Remove the lowest integer in y
        a = sum(y)                          # Sum up the remaining values in y
        b.append(a)                         # Add value to the vector b to displayed and summed when the loop is complete
    print(b)                                # Print the vector y, a.k.a. the stat values
    print('Sum of Stats: ' + str(sum(b)))   # Print the sum total of the stat values
    print()                                 # Print a space for easier viewing of stats

for i in range(3):
    StatRoller()
