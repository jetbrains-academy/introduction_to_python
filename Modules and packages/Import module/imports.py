import calculator
import my_module

calc = calculator.Calculator()  # create new instance of Calculator class defined in calculator module
calc.add(2)
print(calc.get_current())

my_module.hello_world("John")
