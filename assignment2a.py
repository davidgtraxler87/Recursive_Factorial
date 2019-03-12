
def factorial(n):
    if (n <= 1):
        return 1
    else:
        return n * factorial(n - 1)


n = int(input("Choose a number for n: "))
try:
    print ("Result:", factorial(n))
except RecursionError:
    print("Result: The number is too large.")
