'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

user_string = input("type a word or short phrase: ")
as_list = user_string.split(" ")
count_list = []
for item in as_list:
    count_list.append(as_list.count(item))



print("Highest number in occurance-list: " + str(max(count_list)))
highest_occurance = (max(count_list))
'''
find the highest number in count list, determine it's position in the list, and then use its posiion as the index for the word list.
this will find the word with the most occurnaces
'''
highest_occurance_index = (count_list.index(highest_occurance))
most_frequent_word = (as_list[highest_occurance_index]) #value at index of highest occurance
print(f'the word that occurs the most is "{most_frequent_word}"')