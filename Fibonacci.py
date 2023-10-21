#!/usr/bin/python3
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

sum_fibonacci = sum(fibonacci(50))
print(f"The sum of the first 50 Fibonacci numbers is: {sum_fibonacci}")
