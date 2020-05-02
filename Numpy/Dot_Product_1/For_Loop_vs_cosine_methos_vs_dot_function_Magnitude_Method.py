import numpy as np

np_array_1 = np.array([1, 2, 3])
np_array_2 = np.array([3, 2, 1])

# In-oder to find out the angle between the vectors we need to perform following steps of actions
# a.b =  |a| × |b| × cos(θ)
# Magnitude of np_array_1 = np.linalg.norm(np_array_1)
# Magnitude of np_array_2 = np.linalg.norm(np_array_2)
# cos angle between the vectos = np.dot(np_array_1, np_array_2) / (np.linalg.norm(np_array_1) * np.linalg.norm(np_array_2))
# arc angle from the available angle data = np.arccos(cos_Q)
cos_Q = np.dot(np_array_1, np_array_2) / (np.linalg.norm(np_array_1) * np.linalg.norm(np_array_2))
Dot_Product = np.linalg.norm(np_array_1) * np.linalg.norm(np_array_2) * np.arccos(cos_Q)
print('Dot_Product by the magnitude method  :  %s'%Dot_Product)
