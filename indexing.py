import numpy as np
arr = np.array([[10,20,30],
 [40,50,60],
 [70,80,90]])

print("First row:\n", arr[0]) 
print("Last column:\n", arr[:, -1])
print("Element 50:\n", arr[1, 1])
print("Subarray (first two rows and first two columns):\n", arr[:2, :2])
print("Reversed order:\n", arr[::-1, ::-1])