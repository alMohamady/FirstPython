from numpy import *

arr0 = array([11, 22, 33, 44, 55])
arrZ = arr0.copy()

arr0[1] = 88

print(arr0)
print(arrZ)

print(id(arr0))
print(id(arrZ))



