# Noah Hanshaw
# 09/25/2020
# CISC 1305

# First we will list the first two numbers in the series (n1, n2), the final number(nf), and establish a counter for the loop
n1 = 0
n2 = 1
nf = 10
counter = 0
# Now we begin the loop
while counter < nf:
    print(n1)
    nth = n1 + n2
    # Values are updated here
    n1 = n2
    n2 =nth
    counter += 1