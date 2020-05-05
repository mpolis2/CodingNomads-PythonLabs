'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

A = 5

B = float(A)

print (A / B)

C = input ("type a number: ")
D = input ("and another: ")

print(f'{C} x {D} is {int(C)*int(D)}')