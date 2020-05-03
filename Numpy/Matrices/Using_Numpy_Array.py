import numpy as np

Numpy_Array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
Numpy_Array_1 = Numpy_Array * 2

print("Value of 'Numpy_Array' variable is   :   \n%s" % Numpy_Array)
print("\n'Numpy_Array[0][0]'   :   %s" % Numpy_Array[0][0])
print("\n'Numpy_Array[0,0]'   :   %s" % Numpy_Array[0, 0])
print("\nTranspose of Numpy_Array :   \n%s" % Numpy_Array.T)
print("\nPrint '0'th Column value of Matrix    :   %s" % Numpy_Array[:, 0])
print("\nPrint '1'th Column value of Matrix    :   %s" % Numpy_Array[:, 1])
print("\nPrint '2'th Column value of Matrix    :   %s" % Numpy_Array[:, 2])
print("\nPrint '0'th row value of Matrix    :   %s" % Numpy_Array[0, :])
print("\nPrint '1'th row value of Matrix    :   %s" % Numpy_Array[1, :])
print("\nPrint '2'th row value of Matrix    :   %s" % Numpy_Array[2, :])
print("\nExponential function application to 'Numpy_Array'    :   \n%s" % np.exp(Numpy_Array))

# Matrices Multiplication
print("Multiplication result of matrices    :   \n%s    x   %s  =   %s" % (Numpy_Array, Numpy_Array_1,
                                                                           np.dot(Numpy_Array, Numpy_Array_1)))
# Matrices Addition
print("Addition result of matrices    :   \n%s    +   %s  =   %s" % (Numpy_Array, Numpy_Array_1,
                                                                     Numpy_Array + Numpy_Array_1))
# Matrices Division
print("Division result of matrices    :   \n%s    /   %s  =   %s" % (Numpy_Array, Numpy_Array_1,
                                                                     Numpy_Array / Numpy_Array_1))

# Matrices Subtraction
print("Subtraction result of matrices    :   \n%s    -   %s  =   %s" % (Numpy_Array, Numpy_Array_1,
                                                                        Numpy_Array - Numpy_Array_1))

# Metrics Determinant
print("Determinant of 'Numpy_Array' is     :   %s" % np.linalg.det(Numpy_Array))

# Metrics Inverse
try:
    print("Inverse of 'Numpy_Array' is     :   %s" % np.linalg.inv(Numpy_Array))
except Exception as E:
    print('No inverse found :   %s' % E)

# Trace Operation
print("Trace of 'Numpy_Array' is     :   %s" % np.trace(Numpy_Array))
print("Trace of 'Numpy_Array_1' is     :   %s" % np.trace(Numpy_Array_1))

# Diagonal Element Operation
print("Diagonal Element of 'Numpy_Array' is     :   %s" % np.diag(Numpy_Array))
print("Diagonal Element of 'Numpy_Array_1' is     :   %s" % np.diag(Numpy_Array_1))

'''# Eigen Value
print("Eigen Value of 'Numpy_Array' is     :   %s" % np.linalg.eig(Numpy_Array))
print("Eigen Value of 'Numpy_Array_1' is     :   %s" % np.linalg.eig(Numpy_Array_1))'''
