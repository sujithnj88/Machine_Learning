Array_Element = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Type of 'Array_Element' Variable   :   %s" % type(Array_Element))
for i in range(len(Array_Element)):
    print("'Array_Element[%d]'      :   %s" % (i, Array_Element[i]))

for i in range(len(Array_Element)):
    for j in range(len(Array_Element[i])):
        print("'Array_Element[%d][%d]'      :   %s" % (i, j, Array_Element[i][j]))
