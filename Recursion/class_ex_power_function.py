def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n-1)


x = power(3, 3)
print(x)
