from numpy import *

mat = array([
            [1, 2, 3, 7, 8, 9],
            [4, 5, 6, 11, 12, 13]
            ])

m1 = matrix("1 2 3 ; 4 5 6 ; 7 8 9")
m2 = matrix("1 2 3 ; 4 5 6 ; 7 8 9")

m3 = m1 + m2
print(m3)
print(m1.min())
print(diagonal(m1))
mat2 = mat.flatten()
mat3 = mat.reshape(2, 2, 3)

print(mat3)

print(mat)
print(mat2)
print(mat.shape)
print(mat.size)
print(mat.ndim)

