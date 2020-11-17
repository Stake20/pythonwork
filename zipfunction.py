list1 = [1,2,3,4,5]
list2 = ['one', 'two', 'three', 'four', 'five']

zipped = list(zip(list1, list2))
print(zipped)
unzipped = list(zip(*zipped))
print(unzipped)

fruits = ['Guava', 'Naartjie', 'Tomato']
amount_of_fruits = [7, 12, 30]
prices = [12.50, 6.80, 88,88]

what_i_bought = []
for (fruit, amount, price) in zip(fruits, amount_of_fruits, prices):
    amount, price = str(amount), str(price)
    bought = f'I bought {fruit} {amount}s at {price} cents each.'
    what_i_bought.append(bought)

print(what_i_bought)
