'''
Print out every prime number between 1 and 100.

'''

for i in range (1,101):
# check for any even divisor
    if  i==2 or i == 5 or i == 7 or i == 11:
        print(i)
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0 or i % 11 == 0 or i % 2 == 0:
        continue
    else:
        print(i)

