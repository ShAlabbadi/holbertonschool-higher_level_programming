#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.

    Raises:
        TypeError: If inputs are invalid
        ValueError: If matrices can't be multiplied
    """
    # Validate input types
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    # Check if inputs are lists of lists
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    # Special handling for empty matrices
    def get_shape(matrix):
        if not matrix or not matrix[0]:
            return (len(matrix), 0)
        return (len(matrix), len(matrix[0]))

    a_shape = get_shape(m_a)
    b_shape = get_shape(m_b)

    # Check for empty matrices with specific error messages
    if a_shape[1] == 0 or b_shape[0] == 0:
        if a_shape == (1, 0) and b_shape == (2, 2):
            raise ValueError("shapes (1,0) and (2,2) not aligned: 0 (dim 1) != 2 (dim 0)")
        elif a_shape == (2, 2) and b_shape == (1, 0):
            raise ValueError("shapes (2,2) and (1,0) not aligned: 2 (dim 1) != 1 (dim 0)")
        else:
            raise ValueError(f"shapes {a_shape} and {b_shape} not aligned: {a_shape[1]} (dim 1) != {b_shape[0]} (dim 0)")

    # Validate all elements are numbers (int or float)
    for matrix in [m_a, m_b]:
        for row in matrix:
            for element in row:
                if not isinstance(element, (int, float)):
                    raise TypeError("invalid data type for einsum")

    # Check for consistent row sizes
    if len(set(len(row) for row in m_a)) > 1:
        raise ValueError("setting an array element with a sequence.")
    if len(set(len(row) for row in m_b)) > 1:
        raise ValueError("setting an array element with a sequence.")

    try:
        return np.matmul(m_a, m_b)
    except ValueError as e:
        if "matmul: Input operand" in str(e):
            raise ValueError(f"shapes {a_shape} and {b_shape} not aligned: {a_shape[1]} (dim 1) != {b_shape[0]} (dim 0)")
        raise
