import numpy as np
#numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
a = np.array([1,2,3])
print(a)

# 2-D
a2 = np.array([1,2], [3,4])
print('两维数组:\n', a2)

#指定2d
a2_1 = np.array([1,2,3,4,5], ndmin = 2)
print('指定两维:\n', a2_1)

#dtype
a_dtype = np.array([1, 2, 3], dtype = complex)
print(a_dtype)