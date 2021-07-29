class Complex:
    def create(self, real_part, imag_part):
        self.r = real_part
        self.i = imag_part

    def build(self):
        self.num = complex(self.r, self.i)


complex_number = Complex()  # Instantiate a complex number object
complex_number.create(12, 5)  # Call create method with real_part = 12 and imag_part = 5
complex_number.build()  # Build the complex number
print(complex_number.num)


class Calculator:
    current = 0

    def add(self, amount):
        self.current += amount

    def get_current(self):
        return self.current


my_value = Calculator()
my_value.add(100500)
print(my_value.get_current())
