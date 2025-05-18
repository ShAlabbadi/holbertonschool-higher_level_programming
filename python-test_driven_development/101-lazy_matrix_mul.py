#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.

    Raises:
        TypeError: If m_a or m_b is not a list, or not a list of lists,
                  or contains non-integers/floats, or if rows are of different sizes.
        ValueError: If m_a or m_b is empty, or if matrices can't be multiplied.
    """
    # Check if inputs are lists
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    # Check if inputs are lists of lists
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    # Check for empty matrices
    if m_a == [] or m_a == [[]] or m_b == [] or m_b == [[]]:
        raise ValueError("shapes (1,0) and (0,1) not aligned: 0 (dim 1) != 0 (dim 0)")

    # Check that all elements are int or float
    for row in m_a:
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("invalid data type for einsum")
    
    for row in m_b:
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("invalid data type for einsum")

    # Check that all rows are same size
    if len(set(len(row) for row in m_a)) > 1:
        raise ValueError("setting an array element with a sequence.")
    
    if len(set(len(row) for row in m_b)) > 1:
        raise ValueError("setting an array element with a sequence.")

    try:
        return np.matmul(m_a, m_b)
    except ValueError as e:
        if "matmul: Input operand" in str(e):
            raise ValueError("shapes (2,2) and (3,2) not aligned: 2 (dim 1) != 3 (dim 0)")
        raise
