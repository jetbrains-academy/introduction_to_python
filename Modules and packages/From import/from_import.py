from calculator import Add
from my_module import hello as hey


calc = Add()  # Name `Calculator` used directly without prefix `calculator`
calc.add(2)
print(calc.get_current())


print(hey("User"))
