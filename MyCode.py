from functools import reduce

def func(a, b):
    return a * b;
#result = lambda a, b : a * b
#print(result(2, 3))

def isEven(n):
    return n % 2 == 0

nums = [3, 2, 8, 7, 9, 10, 12, 20]
eN = list(filter(lambda n: n % 2 == 0, nums))
print(eN)

doulbles = list(map(lambda n: n * 2, nums))
print(doulbles)

sum = reduce(lambda a, b: a + b, nums)
print(sum)