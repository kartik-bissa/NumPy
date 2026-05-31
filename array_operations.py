import numpy as np
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

added = a + b
subtracted = a - b
multiplied = a * b
divided = a/b
print("Mean of a: \n", np.mean(a))
print("Max of b: \n", np.max(b))
print("Sum of elements in b: \n", np.sum(b))

c = np.array([[1,2,3], [4,5,6]])
print("Row wise sum: \n", np.sum(c, axis=1))
print("Column wise sum: \n", np.sum(c, axis=0))