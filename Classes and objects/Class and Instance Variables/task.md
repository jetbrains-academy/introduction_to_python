## Class and Instance Variables

In general, instance variables are for data unique to each instance, 
and class variables are for attributes and methods shared by all instances of the class:

```python
class Cat:

    species = "Felis catus"  
    
    def __init__(self, breed, name):
        self.breed = breed  
        self.name = name

cleo = Cat('mix', 'Cleo')
furry = Cat('bengal', 'Furry')

print(cleo.name)
print(cleo.species)
print(furry.name)
print(furry.species)
```

```text
Cleo
Felis catus
Furry
Felis catus
```
You can see that `species` is a class variable shared by all instances, while
`name` and `breed` are instance variable unique to each instance.

Shared data can have possibly surprising effects when involving mutable objects, 
such as lists and dictionaries. If a class variable is a list and you modify it for
one object, it will be changed for all objects of the class (check out the example in the code
editor – see what `print(barsik.favorite_food)` will print). If you intend using a list to keep track 
of features unique to each instance, you need to make it an instance attribute.

In the code editor, complete the implementation of the `Animals` class so that the `print` statement 
below prints a line like this: `"This is Doggy the dog, one of my pets."`

<div class="hint">The class variable should contain information shared between all instances.</div>
<div class="hint">Instance variables should contain information unique for the instances.</div>
