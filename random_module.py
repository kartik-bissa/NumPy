import numpy as np

# 1. Set seed
np.random.seed(42)

# 2. Generate 20 random marks between 0 and 100
marks = np.random.randint(0, 100, size=20)

# 3. Print marks and statistics
print("Marks:")
print(marks)

print("\nMean:", marks.mean())
print("Maximum:", marks.max())
print("Minimum:", marks.min())

# 4. Students scoring above 75
print("\nMarks above 75:")
print(marks[marks > 75])

# 5. Failed students (<35)
print("\nFailed students:")
print(marks[marks < 35])

# 6. Give grace marks
marks[marks < 35] = 35

# 7. Modified array
print("\nMarks after grace marks:")
print(marks)