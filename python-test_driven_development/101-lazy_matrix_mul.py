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

    # Check for empty matrices
    if m_a == [] or m_a == [[]] or m_b == [] or m_b == [[]]:
        raise ValueError("shapes (1,0) and (0,1) not aligned: 0 (dim 1) != 0 (dim 0)")

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
            a_shape = (len(m_a), len(m_a[0])) if m_a and m_a[0] else (len(m_a), 0)
            b_shape = (len(m_b), len(m_b[0])) if m_b and m_b[0] else (len(m_b), 0)
            raise ValueError(f"shapes {a_shape} and {b_shape} not aligned: {a_shape[1]} (dim 1) != {b_shape[0]} (dim 0)")
        raise
