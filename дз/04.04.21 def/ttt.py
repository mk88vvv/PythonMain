def pow(a, n):
    if n == 0:
        return 1
    elif n > 0:
        return a * pow(a, n - 1)
    elif n < 0:
        return pow(a, n + 1)/a
print(pow(10,-5))