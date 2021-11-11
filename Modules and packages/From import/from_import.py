from calculator import Calculator
from my_module import hello as hey

print(hey("User"))

calc = Calculator()  # Name `Calculator` used directly without prefix `calculator`
calc.add(2)
calc.multiply(100)
calc.divide(3)

print(calc.get_current())



