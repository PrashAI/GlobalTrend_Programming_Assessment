# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 12:58:58 2024

@author: prasa
"""

def transpose_matrix(matrix):
    """
    Transpose a 2D list (matrix).

    Parameters:
    matrix (list of list of int/float): The 2D list to be transposed.

    Returns:
    list of list of int/float: The transposed 2D list (matrix).
    """
    # Check if the matrix is empty
    if not matrix or not matrix[0]:
        return []

    # Use list comprehension to transpose the matrix
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    
    return transposed

# Example usage:
matrix = [
    [16, 18, 20],
    [24, 25, 26],
    [37, 38, 39]
]

transposed_matrix = transpose_matrix(matrix)
print("Original matrix:")
for row in matrix:
    print(row)

print("\nTransposed matrix:")
for row in transposed_matrix:
    print(row)
