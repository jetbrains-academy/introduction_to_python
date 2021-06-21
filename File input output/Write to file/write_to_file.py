zoo = ["lion", "elephant", "monkey"]
number = 15

if __name__ == "__main__":
    with open("output.txt", 'a') as f:
        f.write('\n' + ' and '.join(zoo))
        f.write('\n' + str(number))


