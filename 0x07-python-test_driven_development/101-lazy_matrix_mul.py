#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Function to multiply two matrices using NumPy.

    Args:
        m_a (list): The first matrix represented as a nested list.
        m_b (list): The second matrix represented as a nested list.

    Returns:
        np.ndarray: The resulting matrix after the multiplication.

    Raises:
        ValueError: If the matrices cannot be multiplied.
    """

    return (np.matmul(m_a, m_b))
