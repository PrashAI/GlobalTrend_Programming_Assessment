# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 12:31:16 2024

@author: prasa
"""

import time
import logging
from functools import lru_cache

# Configure logging
logging.basicConfig(level=logging.INFO)

def timing_decorator(func):
    """
    Decorator that measures the execution time of a function and logs it.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"Execution time of {func.__name__}: {execution_time:.4f} seconds")
        return result
    return wrapper

# Memoized recursive Fibonacci function
@timing_decorator
@lru_cache(maxsize=None)
def compute_fibonacci_memoized(n):
    """
    Function to compute the nth Fibonacci number using memoization.
    """
    if n <= 0:
        raise ValueError("The input must be a positive integer.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return compute_fibonacci_memoized(n - 1) + compute_fibonacci_memoized(n - 2)

# Example usage:
n = 30
print(f"The {n}th Fibonacci number is: {compute_fibonacci_memoized(n)}")
