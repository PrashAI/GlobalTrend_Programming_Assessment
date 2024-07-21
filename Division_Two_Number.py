# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 12:23:35 2024

@author: prasa
"""

def divide_numbers(numerator, divisor):
    """
    Divide two numbers and handle division by zero.

    Parameters:
    numerator (float): The numerator of the division.
    divisor (float): The divisor of the division.

    Returns:
    float or str: The result of the division or a custom error message if the divisor is zero.
    """
    try:
        result = numerator / divisor
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

# Example usage:
numerator = 10
divisor = 0
print(f"Result of {numerator} / {divisor}: {divide_numbers(numerator, divisor)}")

divisor = 2
print(f"Result of {numerator} / {divisor}: {divide_numbers(numerator, divisor)}")
