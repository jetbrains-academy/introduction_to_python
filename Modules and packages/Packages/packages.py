import functions.goodbye as bye
import functions.greeting.hello
from classes import calculator
import functions.greeting.official as official


print(functions.greeting.hello.hello('Susan'))
print(bye.good_bye('Alex'))

c = calculator.Calculator()
c.add(2)
c.multiply(10)
print(c.get_current())

print(official.hello('Sam'))
