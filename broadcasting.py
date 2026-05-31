import numpy as np
a = np.array([[1,2,3], [4,5,6]])
b = np.array([10,20,30])

added = a + b
print("Added: \n", added)

c = np.array([[100], [200]])

added2 = a + c
print("Added a with c: \n", added2)

print("Shape of a: ", a.shape)
print("Shape of b: ", b.shape)      
print("Shape of c: ", c.shape)