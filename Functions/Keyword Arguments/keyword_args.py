def cat(food, state='still hungry', action='meow', breed='Siamese'):
    print(f"-- This cat wouldn't {action}", end=' ')
    print(f"if you gave it {food}")
    print(f"-- Lovely fur, the {breed}")
    print(f"-- It's {state}!")


cat('soup', action='growl', breed='Sphinx')
