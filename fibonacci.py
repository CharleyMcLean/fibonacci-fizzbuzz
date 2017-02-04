"""Write a program generating the first n Fibonacci numbers
F(n), printing:
- "Buzz" when F(n) is divisible by 3
- "Fizz" when F(n) is divisible by 5
- "FizzBuzz" when F(n) is divisible by 15
- "BuzzFizz" when F(n) is prime
- the value of F(n) otherwise
"""

import math


def F(n):
    """Function to find nth Fibonacci number and return
    a specified value"""
    nth_fib = find_nth_fibonacci(n)

    prime = is_prime(nth_fib)

    # check if number is 0 or 1 first
    if nth_fib in range(3):
        return nth_fib

    # Check if divisible by 15 first, then by 3 and 5,
    # otherwise the wrong thing will be returned
    if nth_fib % 15 == 0:
        return "FizzBuzz"
    if nth_fib % 3 == 0:
        return "Buzz"
    if nth_fib % 5 == 0:
        return "Fizz"
    if prime:
        return "BuzzFizz"

    return nth_fib


def find_nth_fibonacci(n):
    """Find nth term of Fibonacci sequence"""
    Phi = (math.sqrt(5) + 1) / 2
    phi = Phi - 1

    # return an integer value
    return int((Phi**n - (-1 * phi)**n) / math.sqrt(5))


def is_prime(n):
    """Determine if number is prime"""
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            continue

    return prime