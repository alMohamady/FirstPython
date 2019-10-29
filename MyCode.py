import sys

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

count = 0

def func():
    global count
    print("Hello world " , count)
    count += 1
    func()

func()

#fibonacci sequence
def func(max):

    x = 0
    y = 1

    print(x)
    print(y)

    for i in range(2, max):
        z = x + y
        x = y
        y = z
        print(z)

func(20)
