# Noah Hanshaw
# CISC 1305 Python 3
# 09/04/2020

# First, we have to import stored math function pi
from math import pi
# The radius value will be stored under the variable r
r = float(input('Please input the radius of the circle: '))
# Now we display the variable given. To prevent an error, we use str() to convert r to a string
print('r=' + str(r))
# Finally, we can print out the final result using the formula for the area of a circle, pi*r^2. Exponents are denoted **
print(pi*r**2)