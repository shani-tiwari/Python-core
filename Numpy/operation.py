# slicing, indexing, stacking on vector and 2d arrays 

#  slicing on vector
import numpy as np

vec = np.array([1, 2, 3, 4, 5])
print(vec[1:3])   # [2 3]
print(vec[:3])    # [1 2 3]
print(vec[3:])    # [4 5]
print(vec[:])     # [1 2 3 4 5]
print(vec[::-1])  # [5 4 3 2 1]

# indexing on vector
print(vec[0])     # 1
print(vec[1])     # 2
print(vec[2])     # 3
print(vec[3])     # 4
print(vec[4])     # 5

# indexing on 2d array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[0, 0])  # 1
print(arr[0, 1])  # 2
print(arr[0, 2])  # 3

# stacking on vector
vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])
print(np.concatenate((vec1, vec2)))  # [1 2 3 4 5 6]
print(np.hstack((vec1, vec2)))      # [1 2 3 4 5 6]
print(np.vstack((vec1, vec2)))      # [ [1 2 3] [4 5 6] ]

# stacking on 2d array
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
print(np.concatenate((arr1, arr2)))  # [[ 1  2  3] [ 4  5  6] [ 7  8  9] [10 11 12]]
print(np.vstack((arr1, arr2)))      # [[ 1  2  3] [ 4  5  6] [ 7  8  9] [10 11 12]]
print(np.hstack((arr1, arr2)))      # [[ 1  2  3  7  8  9] [ 4  5  6 10 11 12]]

# broadcasting on 2d array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr + 1)  # [[2 3 4] [5 6 7] [8 9 10]]
print(arr * 2)  # [[2 4 6] [8 10 12] [14 16 18]]
print(arr - 1)  # [[0 1 2] [3 4 5] [6 7 8]]
print(arr / 2)  # [[0.5 1.  1.5] [2.  2.5 3. ] [3.5 4.  4.5]]


