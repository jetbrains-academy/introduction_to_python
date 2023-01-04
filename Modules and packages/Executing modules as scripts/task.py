import some_module

print(f'This is a message from {__name__}.')
some_module.func()

# Make a change here.
if __name__ == "__main__":
    print('This should be printed ONLY when dict_keys.py is called directly.')

