
def person(name, **data):
    print(name)
    print(data)
    for a,b in data.items():
        print(a, b)

person("ahmed", age=33, secound="Mohamady", length=185.5)