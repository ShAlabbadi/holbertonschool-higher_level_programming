#!/usr/bin/python3
"""Matrix multiplication using NumPy with precise error formatting."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices with exact error message formatting.
    
    Args:
        m_a: First matrix (list of lists)
        m_b: Second matrix (list of lists)
    
    Returns:
        Product matrix as numpy array
    
    Raises:
        ValueError: For shape mismatches
    """
    try:
        np_a = np.array(m_a)
        np_b = np.array(m_b)
        return np.matmul(np_a, np_b)
    except ValueError as e:
        if "matmul: Input operand" in str(e):
            # Format shapes without spaces
            a_shape = f"({len(m_a)},{len(m_a[0])})" if m_a and m_a[0] else f"({len(m_a)},0)"
            b_shape = f"({len(m_b)},{len(m_b[0])})" if m_b and m_b[0] else f"({len(m_b)},0)"
            raise ValueError(
                f"shapes {a_shape} and {b_shape} not aligned: "
                f"{a_shape.split(',')[1][:-1]} (dim 1) != {b_shape.split(',')[0][1:]} (dim 0)"
            )
        raise
