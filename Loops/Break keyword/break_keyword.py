count = 0

while True:  # This condition cannot possibly be false
    print(count)
    count += 1
    if count >= 5:
        break           # Exit loop if count >= 5


zoo = ["lion", "tiger", "elephant", "giraffe", "python"]
while True:                         # This condition cannot possibly be false
    animal = zoo.pop()       # Extract one element from the end of the list
    print(animal)
    if animal == "elephant":
        break

print(zoo)
