import numpy as np

matrix = np.array(
    [[11, 12, 13, 14], [15, 16, 17, 18], [19, 20, 21, 22], [23, 24, 25, 26]]
)

m = np.reshape(matrix, (4, 4))

# print(m)

# accessing element

# print(matrix[2])
# print(matrix[2][3])

# adding elements
m = np.append(m, [[33, 32, 31, 30]], 0)
# print(m)

# deleting elements
m = np.delete(m, [4], 0)
print(m)
