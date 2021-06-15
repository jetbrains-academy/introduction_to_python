class Complex:
    def __init__(self, real_part, imag_part):
        self.real = real_part
        self.img = imag_part

    def __repr__(self):
        return f'Complex(10, 20)'

    def __str__(self):
        return f'{self.real} + i{self.img}'


x = Complex(2, 5)
print(str(x))
print(repr(x))


class Cat:
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def __repr__(self):
        return f'Cat, breed: {self.breed}, name: {self.name}'

    def __str__(self):
        return f'My {self.breed} cat\'s name is {self.name}'


lucy = Cat('siamese', 'Lucy')
print(str(lucy))
print(repr(lucy))
