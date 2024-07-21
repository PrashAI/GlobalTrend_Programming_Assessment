# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 12:19:55 2024

@author: prasa
"""

def fibonacci(n):
    """
    Compute the nth Fibonacci number using recursion.

    Parameters:
    n (int): The position of the Fibonacci number to compute.

    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 0:
        raise ValueError("The input must be a positive integer.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage:
n = 10
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
