zoo = ["lion", "elephant", "monkey"]
number = 15

with open("output.txt", 'a') as f:
    f.write('\n' + ' and '.join(zoo))
    f.write('\n' + str(number))


