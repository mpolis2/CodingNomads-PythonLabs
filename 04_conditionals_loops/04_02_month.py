'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''

months = ["January", "February", "March", "April", "May", "June", "July", "August",
          "September", "October", "November", "December"]
number = int(input("type a number: "))
if number <= 12:
    print(months[number-1])
elif number > 12:
    print("Other")
