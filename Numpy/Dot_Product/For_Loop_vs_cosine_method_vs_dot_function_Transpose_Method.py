import numpy as np

np_array_1 = np.array([1, 2, 3])
np_array_2 = np.array([3, 2, 1])

# Dot product using for loop
dot = 0
for i, j in zip(np_array_1, np_array_2):
    dot += i * j
print('Dot Product using for loops  :   %s' % dot)

# Dot product using np instance methods
''' # 1. sum instance method '''
print('Dot Product using for sum instance method  :   %s' % np.sum(np_array_1*np_array_2))
print('Dot Product using for sum instance method  :   %s' % (np_array_1*np_array_2).sum())

''' # 2. dot instance method '''
print('Dot Product using for dot instance method  :   %s' % np.dot(np_array_1,np_array_2))
print('Dot Product using for dot instance method  :   %s' % np_array_1.dot(np_array_2))
print('Dot Product using for dot instance method  :   %s' % np_array_2.dot(np_array_1))
