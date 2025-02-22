# example.py

def factorial_generator(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result


gen = factorial_generator(5)

for value in gen:
    print(value)
