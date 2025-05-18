#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.

    Raises:
        ValueError: For scalar operands, shape mismatches, empty matrices
        TypeError: For None inputs and invalid data types
    """
    # Handle None inputs first
    if m_a is None or m_b is None:
        raise TypeError("Object arrays are not currently supported")

    # Validate input types
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    # Check if inputs are lists of lists
    flat_a = isinstance(m_a, list) and not isinstance(m_a[0], list)
    flat_b = isinstance(m_b, list) and not isinstance(m_b[0], list)
    if (not all(isinstance(row, list) for row in m_a) or
            not all(isinstance(row, list) for row in m_b)):
        if flat_a and flat_b:
            msg = f"shapes ({len(m_a)},) and ({len(m_b)},) not aligned: "
            msg += f"{len(m_a)} (dim 0) != {len(m_b)} (dim 0)"
            raise ValueError(msg)
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    # Get matrix shapes without spaces
    def get_shape(matrix):
        if not matrix or not matrix[0]:
            return f"({len(matrix)},0)"
        return f"({len(matrix)},{len(matrix[0])})"

    a_shape = get_shape(m_a)
    b_shape = get_shape(m_b)

    # Check for empty matrices
    if a_shape.endswith(",0)") or b_shape.startswith("(0,"):
        dim1 = a_shape.split(',')[1][:-1]
        dim0 = b_shape.split(',')[0][1:]
        msg = f"shapes {a_shape} and {b_shape} not aligned: "
        msg += f"{dim1} (dim 1) != {dim0} (dim 0)"
        raise ValueError(msg)

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
            dim1 = a_shape.split(',')[1][:-1]
            dim0 = b_shape.split(',')[0][1:]
            msg = f"shapes {a_shape} and {b_shape} not aligned: "
            msg += f"{dim1} (dim 1) != {dim0} (dim 0)"
            raise ValueError(msg)
        raise
