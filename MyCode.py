
def add(*b):
    c = 0
    for i in b:
        c += i
    print(c)

add(10, 5, 6, 7, 8)

def one(name, age = 18):
    print(name)
    print((age - 1) /2)

one(name='al Mohamady')
