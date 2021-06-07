def cat(food, state='still hungry', action='meow', breed='Siamese'):
    print("-- This cat wouldn't", action, end=' ')
    print("if you gave it", food)
    print("-- Lovely fur, the", breed)
    print("-- It's", state, "!")


cat('soup', action='growl', breed='Sphinx')
