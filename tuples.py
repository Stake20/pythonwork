
coordinates = (4, 5)
# coordinates[1] = 10   will recieve an error, tuples are immutable
print(coordinates[0], type(coordinates))

fruits = ('Apples', 'Oranges', 'Grapes')

#Single value needs trailing coma
fruits2 = ('Apples',)

print(fruits2, type(fruits2))

del fruits2
# print(fruits2)

print(len(fruits))