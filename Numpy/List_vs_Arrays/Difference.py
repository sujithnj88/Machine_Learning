import numpy as np

List_Test = [1, 2, 3, 4, 5, 6]
Numpy_Array = np.array(List_Test)

print("Type of List_Test   :   %s" % type(List_Test))
print("List_Test    :   %s" % List_Test)
print("Type of Numpy_Array   :   %s" % type(Numpy_Array))
print("Numpy_Array    :   %s" % Numpy_Array)
print("##########################################################################")

print('\n###################################################\n"+" operator on List and Numpy array')
print('###################################################')
# List  :   "+" operator performs list concatenation
# Numpy Array   : "+" operator performs vector addition
List_Test.append(7)
print("'+'on List with 7  :   %s"%List_Test)
print("'+'on List with [8,9,10,11]   :   %s"%(List_Test+[8, 9, 10, 11]))
print("'+'on Array with Numpy_Array itself :   %s"%(Numpy_Array+Numpy_Array))

print('\n###################################################\n"*" operator on List and Numpy array')
print('###################################################')
# List  :   '*' operator performs duplication of data in the list
# NUmpy Array   :   '*' operator performs vector multiplication
print("'*'on List with '2'   :   %s" % List_Test*2)
print("'*'on Array with '2' :   %s" % Numpy_Array*2)

print('\n###################################################\n"**" operator on List and Numpy array')
print('###################################################')
# List  "   'Exponential' operation cannot be directly applied. Need to iterate over elements and perform it.
# Numpy Array   "   'Exponential' operation can be directly applied
#################################### LIST #############################################
try:
    print('Exponential OPeration directly on List is Successful :   %s'%(List_Test**2))
except Exception as E:
    print('Exception Occured    :   %s'%E)
    print('Exponential Operation in progress    :   [',end='')
    for i in List_Test:
        if i < len(List_Test):
            print(i**2,end=',')
        else:
            print(i ** 2, end=']\n')
########################################################################################
print('Exponential Operation on Numpy Array   :   %s'%(Numpy_Array**2))
########################################################################################

print('Square root of Numpy array :   %s' % np.sqrt(Numpy_Array))
print('Logarithm of Numpy Array :   %s' % np.log(Numpy_Array))