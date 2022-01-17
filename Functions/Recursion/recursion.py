def factorial(n):
    if n <= 1:
        return 1
    else:
        # calculate n multiplied by the factorial of n - 1
        return n * factorial(n - 1)


print(factorial(12))
