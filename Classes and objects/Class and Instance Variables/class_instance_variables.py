# The `favorite_food` list in the following code should not be used as a
# class variable because a single list would be shared by all `Cat` instances:
class Cat:

    favorite_food = []

    def __init__(self, name):
        self.name = name

    def add_food(self, food):  # Method modifying the class variable
        self.favorite_food.append(food)


kitty = Cat('Kitty')
barsik = Cat('Barsik')
kitty.add_food('salmon')  # We are only adding a fave food for Kitty, but Barsik gets it too
print(barsik.favorite_food)


# Because every cat has its own favorite food,
# this class should be instead implemented as follows:
class Cats:

    def __init__(self, name):
        self.name = name
        self.favorite_food = []

    def add_food(self, food):  # Method modifying an instance variable
        self.favorite_food.append(food)


kitty = Cats('Kitty')
barsik = Cats('Barsik')
kitty.add_food('salmon')
print(barsik.favorite_food)  # This time it's empty!


class Animals:
    # Add a class variable `kind`.
    kind = 'pets'

    def __init__(self, name, species):
        # Add an instance variable `name`.
        self.name = name
        # Add an instance variable `species`.
        self.species = species

    def __str__(self):
        return f'\nThis is {self.name} the {self.species}, one of my {self.kind}.'


george = Animals('George', 'rabbit')
sally = Animals('Sally', 'horse')
print(george, sally)
