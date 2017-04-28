# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 19:33:07 2017
@filename: 05A-Numpy.py
@author: cyruslentin
"""

# Numpy
# Numpy is the core library for scientific computing in Python. It provides a 
# high-performance multidimensional array object, and tools for working with 
# these arrays. 

# Arrays
# A numpy array is a grid of values, all of the same type, and is indexed by a 
# tuple of nonnegative integers. The number of dimensions is the rank of the 
# array; the shape of an array is a tuple of integers giving the size of the 
# array along each dimension.

# We can initialize numpy arrays from nested Python lists, and access elements 
# using square brackets:

import numpy as np

a = np.array([1, 2, 3])             # Create a rank 1 array
print(type(a))                      # Prints "<type 'numpy.ndarray'>"
print(a.shape)                      # Prints "(3,)"
print(a[0], a[1], a[2])             # Prints "1 2 3"
a[0] = 5                            # Change an element of the array
print(a)                            # Prints "[5, 2, 3]"

b = np.array([[1,2,3],[4,5,6]])     # Create a rank 2 array
print(b.shape)                      # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])    # Prints "1 2 4"

    
# Numpy also provides many functions to create arrays:

a = np.zeros((2,2))                 # Create an array of all zeros
print(a)                            # Prints "[[ 0.  0.]
                                    #          [ 0.  0.]]"
b = np.ones((1,2))                  # Create an array of all ones
print(b)                            # Prints "[[ 1.  1.]]"

c = np.full((2,2), 7)               # Create a constant array
print(c)                            # Prints "[[ 7.  7.]
                                    #          [ 7.  7.]]"
d = np.eye(2)                       # Create a 2x2 identity matrix
print(d)                            # Prints "[[ 1.  0.]
                                    #          [ 0.  1.]]"
e = np.random.random((2,2))         # Create an array filled with random values
print(e)                            # Might print "[[ 0.91940167  0.08143941]
                                    #               [ 0.68744134  0.87236687]]"     

# Array indexing
# Numpy offers several ways to index into arrays.

# Slicing: Similar to Python lists, numpy arrays can be sliced. Since arrays may be multidimensional, you must specify a slice for each dimension of the array:

# Create the following rank 2 array with shape (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(a)
# Use slicing to pull out the subarray consisting of the first 2 rows
# and columns 1 and 2; b is the following array of shape (2, 2):
# [[2 3]
#  [6 7]]
b = a[:2, 1:3]
print(b)

# A slice of an array is a view into the same data, so modifying it
# will modify the original array.
print(a[0, 1])                      # Prints "2"
b[0, 0] = 77                        # b[0, 0] is the same piece of data as 
                                    # a[0, 1]
print(a[0, 1])                      # Prints "77"

# You can also mix integer indexing with slice indexing. However, doing so 
# will yield an array of lower rank than the original array. 

# Create the following rank 2 array with shape (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

# Two ways of accessing the data in the middle row of the array.
# Mixing integer indexing with slices yields an array of lower rank,
# while using only slices yields an array of the same rank as the
# original array:
row_r1 = a[1, :]                    # Rank 1 view of the second row of a  
row_r2 = a[1:2, :]                  # Rank 2 view of the second row of a
print(row_r1, row_r1.shape)         # Prints "[5 6 7 8] (4,)"
print(row_r2, row_r2.shape)         # Prints "[[5 6 7 8]] (1, 4)"

# We can make the same distinction when accessing columns of an array:
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape)         # Prints "[ 2  6 10] (3,)"
print(col_r2, col_r2.shape)         # Prints "[[ 2]
                                    #          [ 6]
                                    #          [10]] (3, 1)"

