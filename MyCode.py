

def countList(lst):
    even = 0
    odd = 0

    for i in lst:
        if i % 2 == 0:
            even += i
        else:
            odd += i
    return even, odd


lst = [1, 2, 3, 4, 5, 6, 7]
even, odd = countList(lst)

print(even)
print(odd)