'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
mult_total = 1
numbers = []
for i in range (10):
    new_num = int(input("type in a number: "))
    numbers.append(new_num)
    mult_total *= new_num #running total multiplying each new number

print(f'the largest number is {sorted(numbers)[-1]}')
print(f'multiplying all numbers = {mult_total}')