'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''

#get user words
word_1 = input("Type a word: ")
word_2 = input("Type a 2nd word: ")
word_3 = input("Type a 3rd word: ")

#print words, each with length
print(str(len(word_1)), word_1)
print(str(len(word_2)), word_2)
print(str(len(word_3)), word_3)