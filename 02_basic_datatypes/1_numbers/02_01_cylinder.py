'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''

# V=πr2h
# volume = pi * radius-squared * height

radius = 3.14
height = 5
pi = 3.14
volume = pi * radius ** 2 * height

print (f'volume = {volume}')

#surface area
#A=2πrh+2πr2
# area = (2 * pi * radius * height) + (2 * pi * radius-squared)
area = (2 * pi * radius * height) + (2 * pi * radius ** 2)

print (f'area = {area}')