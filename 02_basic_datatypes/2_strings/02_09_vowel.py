'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''

# get user sentence
sentence = input("type a sentence: ").lower()
# define vowels

A = sentence.count("a")
E = sentence.count("e")
I = sentence.count("i")
O = sentence.count("o")
U = sentence.count("u")

vowels = ['a', 'e', 'i', 'o', 'u']

print(A, E, I, O, U)

print(f"there are {A} a's")
print(f"there are {E} e's")
print(f"there are {I} i's")
print(f"there are {O} o's")
print(f"there are {U} u's")
print(f' {A+E+I+O+U} vowels total')
# locate vowels in sentence

# display totals for each and grand total for all vowells