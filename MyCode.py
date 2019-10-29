def hello():
    print("Hello World")
    print("Al Mohamady")

hello()

def add(x, y):
    n = x + y
    return n

def add_sub(x, y):
    n = x + y
    x = x - y
    return n, x

z, b = add_sub(20, 12)
print("add :",z)
print("sub :",b)
print(add(5, 3) + 2)
print("MY CODE")
