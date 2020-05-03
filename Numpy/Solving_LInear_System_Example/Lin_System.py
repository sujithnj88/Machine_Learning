import numpy as np

a = np.array([[1, 1], [1.5, 4]])
b = np.array([2200, 5050])
x = np.linalg.solve(a, b)

print("Solution of the Linear System    :   ")
print("Number of Children   :   %s  Adults  :   %s" % (x[0], x[1]))
