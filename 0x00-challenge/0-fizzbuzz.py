#!/usr/bin/python3
""" FizzBuzz Algorith
"""

import sys


def fizzbuzz(n):
    """
    The FizzBuzz function displays numbers from 1 to n,
    with each number separated by a space.

    - It replaces multiples of three with "Fizz", and multiples
    of five with "Buzz".
    - If a number is a multiple of both three and five, it prints "FizzBuzz".
    """
    if n < 1:
        return


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    number = int(sys.argv[1])
    fizzbuzz(number)

    tmp_result = []
    for i in range(1, n + 1):
        if (i % 3) == 0 and (i % 5) == 0:
            tmp_result.append("FizzBuzz")
        elif (i % 5) == 0:
            tmp_result.append("Buzz")
        elif (i % 3) == 0:
            tmp_result.append("Fizz")
        else:
            tmp_result.append(str(i))
    print(" ".join(tmp_result))
