# Noah Hanshaw
# CISC 1305 Python 4
# 09/16/2020

# WE first create a list for the program to sort under a
a = [1,2,3,4,5,6,7,8,9,10]
# Now we input the algorithm to search for values less than 5. The program keeps integers if they are less than 5
x = [i for i in a if i<5]
# Finally we print the results
print(x)