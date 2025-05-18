#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.

    Raises:
        ValueError: For scalar operands, shape mismatches, and empty matrices
        TypeError: For None inputs and invalid data types
    """
    # Handle None inputs first
    if m_a is None or m_b is None:
        raise TypeError("Object arrays are not currently supported")

    # Validate input types
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    # Check if inputs are lists of lists
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        # Handle flat lists
        if (isinstance(m_a, list) and not isinstance(m_a[0], list) and
            isinstance(m_b, list) and not isinstance(m_b[0], list)):
            raise ValueError(f"shapes ({len(m_a)},) and ({len(m_b)},) not aligned: {len(m_a)} (dim 0) != {len(m_b)} (dim 0)")
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    # Get matrix shapes
    def get_shape(matrix):
        if not matrix:
            return (len(matrix), 0)
        if not matrix[0]:
            return (len(matrix), 0)
        return (len(matrix), len(matrix[0]))

    a_shape = get_shape(m_a)
    b_shape = get_shape(m_b)

    # Format shapes without spaces for error messages
    def format_shape(shape):
        return f"({shape[0]},{shape[1]})"

    # Check for empty matrices
    if a_shape[1] == 0 or b_shape[0] == 0:
        raise ValueError(f"shapes {format_shape(a_shape)} and {format_shape(b_shape)} not aligned: {a_shape[1]} (dim 1) != {b_shape[0]} (dim 0)")

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
            raise ValueError(f"shapes {format_shape(a_shape)} and {format_shape(b_shape)} not aligned: {a_shape[1]} (dim 1) != {b_shape[0]} (dim 0)")
        raise
