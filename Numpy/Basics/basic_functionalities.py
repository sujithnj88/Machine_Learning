import numpy as np

Numpy_Array = np.arange(15).reshape(3, 5)
print("Generated Array  :   \n%s" % Numpy_Array)

# 1. ndim
print('Number of axes of the array :   %s' % np.ndim(Numpy_Array))

#2. shape
print('Shape of the array :   %s' % Numpy_Array.shape)

# 3. size
print('Size of the array :   %s' % np.size(Numpy_Array))

# 4. dtype
print('dtype name of the array  :   %s' % Numpy_Array.dtype.name)

# 5. iemsize
print('itemsize of the array  :   %s' % Numpy_Array.itemsize)