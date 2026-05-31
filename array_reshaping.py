import numpy as np
arr = np.arange(1,13)
a1 = arr.reshape(3, 4)
a2 = arr.reshape(2, 6)
flat = a1.flatten()
transposed = a1.T
print("Shape of original array:\n", arr.shape)
print("Shape of reshaped array (3, 4):\n", a1.shape)
print("Shape of reshaped array (2, 6):\n", a2.shape)
print("Shape of flattened array:\n", flat.shape)
print("Shape of transposed array:\n", transposed.shape)