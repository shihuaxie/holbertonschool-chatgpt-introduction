#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer using recursion.

    Parameters
    ----------
    n : int
        A non-negative integer whose factorial is to be computed.

    Returns
    -------
    int
        The factorial of the input number n.
        - If n == 0, returns 1 (by definition of factorial).
        - Otherwise, returns n * factorial(n-1).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Read integer input from command line arguments
f = factorial(int(sys.argv[1]))

# Print the computed factorial
print(f)