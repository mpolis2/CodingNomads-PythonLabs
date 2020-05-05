'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''
#get name
name = input("type your name: ")

#get first letter
first_letter = name[0]

#remove first letter
name = name[1:]

#append first letter + 'ay' to end of word
name = name + first_letter + "ay"
print(name)
