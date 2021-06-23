def cuenta_regresiva(n):
    if n > 0:
        print(n)
        cuenta_regresiva(n-1)
    else:
        print(n)

cuenta_regresiva(5)

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

print(factorial(5))