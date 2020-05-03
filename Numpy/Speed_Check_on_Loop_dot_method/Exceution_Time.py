import numpy as np
from datetime import datetime

np_array_1 = np.random.randn(200)
np_array_2 = np.random.randn(200)
Time_Delta = 50000


def Loop_Execution(a,b):
    dot = 0
    for i, j in zip(a, b):
        dot += i * j
    return dot


start = datetime.now()
for i in range(Time_Delta):
    Loop_Execution(np_array_1, np_array_2)
d_end_Loop = datetime.now() - start

start = datetime.now()
for i in range(Time_Delta):
    np.dot(np_array_1, np_array_2)
d_end_dot = datetime.now() - start

print("Execution time of Loop  :   %s" % d_end_Loop.total_seconds())
print("Execution time of dot instance method  :   %s" % d_end_dot.total_seconds())

print("Performance Factor(dot method is faster than loops method by)    :       %s times" % (d_end_Loop.total_seconds()/d_end_dot.total_seconds()))