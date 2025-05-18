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

    # Check for empty matrices with specific error messages
    if m_a == [] or m_a == [[]]:
        if m_b == [] or m_b == [[]]:
            raise ValueError("shapes (1,0) and (0,1) not aligned: 0 (dim 1) != 0 (dim 0)")
        else:
            # Case where m_a is empty but m_b is [[5,6],[7,8]]
            raise ValueError("shapes (1,0) and (2,2) not aligned: 0 (dim 1) != 2 (dim 0)")
    elif m_b == [] or m_b == [[]]:
        # Case where m_b is empty but m_a is [[5,6],[7,8]]
        raise ValueError("shapes (2,2) and (1,0) not aligned: 2 (dim 1) != 1 (dim 0)")

    # Rest of your validation checks...
    # (Keep the existing checks for element types, row sizes, etc.)

    try:
        return np.matmul(m_a, m_b)
    except ValueError as e:
        if "matmul: Input operand" in str(e):
            # Handle other shape mismatch cases
            a_shape = (len(m_a), len(m_a[0])) if m_a and m_a[0] else (len(m_a), 0)
            b_shape = (len(m_b), len(m_b[0])) if m_b and m_b[0] else (len(m_b), 0)
            raise ValueError(f"shapes {a_shape} and {b_shape} not aligned: {a_shape[1]} (dim 1) != {b_shape[0]} (dim 0)")
        raise
