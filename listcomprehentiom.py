names = ['Thabang', 'Timothy', 'Musi', 'Moabi']

list = []
for person in names:
    list.append(person)
print(list)

print([person for person in names])

list = []
for person in names:
    list.append(person + ' is my name.')
print(list)

print([person + ' is my name.' for person in names])

movies_and_rating = {
    'Harry potter': 9,
    'The Avengers': 8,
    'Green Lantern': 5,
    'Miss Pelligrin': 4,
    'Dragonball': 3

}

list = []
for movie in movies_and_rating:
    if movies_and_rating[movie] > 6:
        list.append(movie)
print(list)

print([movie for movie in movies_and_rating if movies_and_rating[movie] > 6])


