class Square:
    def __init__(self):  # Special method __init__
        self.sides = 4


square = Square()
print(square.sides)


class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand


# Note: you should not pass the self parameter explicitly,
# only the color and the brand parameters.
car = Car("blue", "BMW")

print(car.color, car.brand)
