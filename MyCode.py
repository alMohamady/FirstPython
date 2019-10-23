from array import *

arr = array('i', [])

num = int(input("Enter the array count: "))

for i in range(num):
    x = int(input("Enter the value number " + str(i) + " : "))
    arr.append(x)

print(arr)

val = int(input("Enter the value : "))

index = 0
for i in arr:
    if i == val:
        print(str(i) + " With index  " + str(index))
        break
    index += 1


print(str(val) + " With index  " + str(arr.index(val)))