import numpy as np
from datetime import datetime

List_Data_Ref = [[1, 2, 3], [4, 5, 6], [7, 8, 9],[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Numpy_List_Data_Ref = np.array(List_Data_Ref)
# Below code accepts data input from user and performs the metrics creation using list
'''Row = int(input("Enter the Row value for the Metrics :   "))
Column = int(input("Enter the Column value for the Metrics :   "))
List_Data_Ref = []

for i in range(Row):
    Dummy_List = []
    for j in range(Column):
        Dummy_List.append(int(input("Enter the [%s][%s]th element   :   " % (i, j))))
    List_Data_Ref.append(Dummy_List)'''


def Metrics_Multiply_List(Lst, Multiplier):
    Temporary_Result = []
    for i in Lst:
        Temp_Lst = []
        for j in i:
            Temp_Lst.append(j * Multiplier)
        Temporary_Result.append(Temp_Lst)
    return Temporary_Result


start = datetime.now()
for i in range(100000):
    Metrics_Multiply_List(List_Data_Ref, 5)
End_List_Execution_Time = datetime.now() - start

start = datetime.now()
for i in range(100000):
    Numpy_List_Data_Ref*5
End_Numpy_Execution_Time = datetime.now() - start

print("Execution time using List  :   %s" % End_List_Execution_Time.total_seconds())
print("Execution time of Numpy Array  :   %s" % End_Numpy_Execution_Time.total_seconds())

print("Performance Factor(Multiplication of metrics using Numpy is faster than using Lists by )    :       %s times"
       % (End_List_Execution_Time.total_seconds()/End_Numpy_Execution_Time.total_seconds()))