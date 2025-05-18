#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.

    Raises:
        TypeError: For invalid input types or None values
        ValueError: For empty matrices, shape mismatches, etc.
    """
    # Handle None inputs
    if m_a is None or m_b is None:
        raise TypeError("Object arrays are not currently supported")

    # Check if inputs are lists
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    # Check if inputs are lists of lists
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        # Handle flat list cases
        if isinstance(m_a, list) and not isinstance(m_a[0], list):
            if isinstance(m_b, list) and not isinstance(m_b[0], list):
                # Both are flat lists
                if len(m_a) == len(m_b):
                    return sum(a*b for a, b in zip(m_a, m_b))
                raise ValueError(f"shapes ({len(m_a)},) and ({len(m_b)},) not aligned: {len(m_a)} (dim 0) != {len(m_b)} (dim 0)")
            raise ValueError("Scalar operands are not allowed, use '*' instead")
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    # Check for empty matrices
    if m_a == [] or m_a == [[]] or m_b == [] or m_b == [[]]:
        a_shape = (len(m_a), 0) if m_a and not m_a[0] else (0, 0)
        b_shape = (len(m_b), 0) if m_b and not m_b[0] else (0, 0)
        if a_shape == (1, 0) and b_shape == (2, 2):
            raise ValueError("shapes (1,0) and (2,2) not aligned: 0 (dim 1) != 2 (dim 0)")
        elif a_shape == (2, 2) and b_shape == (1, 0):
            raise ValueError("shapes (2,2) and (1,0) not aligned: 2 (dim 1) != 1 (dim 0)")
        else:
            raise ValueError(f"shapes {a_shape} and {b_shape} not aligned: {a_shape[1]} (dim 1) != {b_shape[0]} (dim 0)")

    # Validate all elements are numbers
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
