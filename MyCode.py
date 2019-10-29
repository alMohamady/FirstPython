
#By Ref
def func1(x):
    print(id(x))
    x[1] = 30
    print("x " ,x)
    print(id(x))

lst = [ 10, 12, 14]
print(id(lst))
func1(lst)
print("a ", lst)

#By Val
def func0(x):
    print(id(x))
    x = 10
    print("x " ,x)
    print(id(x))

a = 20
print(id(a))
func0(a)
print( "a ", a)