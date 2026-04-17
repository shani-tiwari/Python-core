# Numpy is a library for numerical operations in Python
# It is used for array manipulation and mathematical operations
# It is a fast and efficient library for numerical operations
# It is a must-have library for data science and machine learning

import numpy as np

# Create a numpy array
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Create a 2D numpy array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

# Create a numpy array with random values
arr3 = np.random.rand(3, 3)
print(arr3)

# Create a numpy array with zeros
arr4 = np.zeros((3, 3))
print(arr4)

# Create a numpy array with ones
arr5 = np.ones((3, 3))
print(arr5)

# Create a numpy array with a range of values
arr6 = np.arange(10) # 0-9
print(arr6)

# Create a numpy array with a range of values with a step
arr7 = np.arange(10, 20, 2) # 10-18 step 2
print(arr7)

# Create a numpy array with a range of values with a step and reshape it
arr8 = np.arange(10, 20, 2).reshape(2, 5) # 2 rows and 5 columns
print(arr8)

# Create a numpy array with a range of values with a step and reshape it to 2x2
arr9 = np.arange(10, 20, 2).reshape(2, 2) # 2 rows and 2 columns
print(arr9)


#  Methods and Attributes
print(arr.shape)         # shape of the array
print(arr.size)          # size of the array
print(arr.ndim)          # dimension of the array
print(arr.dtype)         # data type of the array
print(arr.itemsize)      # size of each item in the array
print(arr.nbytes)        # total size of the array in bytes
print(arr.T)             # transpose of the array
print(arr.real)          # real part of the array
print(arr.imag)          # imaginary part of the array

# Mathematical operations
print(arr.min())         # minimum value of the array
print(arr.max())         # maximum value of the array
print(arr.argmin())      # index of the minimum value of the array
print(arr.argmax())      # index of the maximum value of the array
print(arr.argsort())     # sorted index of the array
print(arr.sort())        # sorted array
print(arr.copy())        # copy of the array
print(arr.view())        # view of the array
print(arr.mean())        # mean of the array
print(arr.conjugate())   # conjugate of the array
print(arr.trace())       # trace of the array
print(arr.sum())         # sum of the array
print(arr.std())         # standard deviation of the array
print(arr.var())         # variance of the array
print(arr.flatten())     # flattened array
print(arr.ravel())       # flattened array
print(arr.reshape(2, 2)) # reshaped array
