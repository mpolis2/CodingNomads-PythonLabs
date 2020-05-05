'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''

sentence = input("type a short sentence: ")
letter = input("now type a single character to locate: ").strip()

print("result")
print(f'the first instance of "{letter}" is located at index[{sentence.find(letter)}]')