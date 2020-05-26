'''
Use a "while" loop to print out every fifth number counting from 1 to 1000.

'''
i = 0
while i <= 1000:
    i += 5
    if i == 1000:
        break
    print(i)
