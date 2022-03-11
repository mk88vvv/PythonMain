n=int(input())
def factorial(n):
    if n >= 1:
        return n * factorial(n - 1)
    elif n == 0:
        return 1

        
factorial(n)
print(factorial(n))