import numpy as np
data = np.array([
    10, -5, 25, -3, 40,
    -8, 60, 15, -1, 80
])

print("All Negative Values:\n", data[data < 0])
print("All Values Greater than 20 : \n", data[data > 20])

data[data < 0] = 0
print("Data after masking negative values: \n", data)

print("Mean of the modified data: ", data.mean())
print("Maximum: ", data.max())
print("Minimum: ", data.min())

print("Values between 10 and 50: \n", data[(data >= 10) & (data <= 50)])