
a = 20
print(id(a))

def func():
    a = 30
    print(id(a))
    x = globals()['a']
    print(id(x))
    print(" FUNC A :", a)
    print(x)


func()
print("GLOBAL A:", a)