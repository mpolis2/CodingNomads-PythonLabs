'''
Write a script that takes a tuple and turns it into a list.

'''

tuple_ = (2, 3, 4, 5)

#method 1 - lop[ & append
#list_=[]
#for item in tuple_:
#    list_.append(item)

#method 2 - explicit type
list_ = list(tuple_)

print(list_)
print(type(list_))