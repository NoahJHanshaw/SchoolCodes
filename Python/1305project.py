# Noah Hanshaw
# CISC 1305 Final Project
# 11/13/2020

# i = Customer ID; n = Customer Name; u = Units used by customer; c = charge; s = surcharge; t = total
i = input('Input the Customer ID: ')                                    # Customer ID Number
n = input('Input the full Customer Name: ')                             # Customer Name
u = (input('Input the number of units used by the customer: '))         # Units used by the customer

if u.isdigit():
    u = float(u)
    print('Customer ID: ' + i)                                          # Printing the Customer ID, Name, and units used
    print('Customer Name: ' + n)
    print('Units used: ' + str(u))
    if u < 0:
        print('ERROR: Input value for units was a negative number. Please input a positive number.')
    elif u < 200:                                                       # Start if loop to determine how much to charge the customer based on units used
        c = round(u*2.21, 2)
        print('Total Cost: $' + str(c))
    elif u < 400:
        c = round(u*2.53, 2)
        print('Totat Cost: $' + str(c))
    elif u < 600:
        c = round(u*2.87, 2)
        print('Total Cost: $' + str(c))
    elif u < 1000:
        c = round(u*3.02, 2)
        print('Total Cost: $' + str(c))
    elif u > 1000:
        c = round(u*3.26, 2)
        print('Total Cost: $' + str(c))
    if c > 500:                                                          # If the charge passes a certain amount, apply 25% of the charge as a surcharge
        s = round(c*.25, 2)
        t = round(c+s, 2)
        print('Surcharge: $' + str(s))                                              # Print Surcharge amount and final total, if applicable
        print('Final Total: $' + str(t))
else:
    print('ERROR: Input value for units was not a number. Please input a number.')
