def print_heart(n):
    for i in range(n // 2, n, 2):
        for j in range(1, n - i, 2):
            print(end="  ")
        for j in range(1, i + 1):
            print("*", end=" ") if (j == 1 or j == i) else print(end="  ")
        for j in range(1, n - i + 1):
            print(end="  ")
        for j in range(1, i + 1):
            print("*", end=" ") if (j == 1 or j == i) else print(end="  ")
        print()

    for i in range(n, 0, -1):
        for j in range(i, n):
            print(end="  ")
        for j in range(1, i * 2):
            print("*", end=" ") if (j == 1 or j == i * 2 - 1 or (i == n and j == i)) else print(end="  ")
        print()


if __name__ == '__main__':
    print_heart(5)
