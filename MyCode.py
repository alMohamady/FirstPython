from array import *

arr = array('i', [5, 6, 7, 8])
arr2 = array('u', ['a', 'b', 'c', 'd'])

arr3 = array(arr.typecode, (a + 10 for a in arr))

for i in arr3:
    print(i)

for i in arr2:
    print(i)

for i in range(len(arr)):
    print(arr[i])

for i in arr:
    print(i)