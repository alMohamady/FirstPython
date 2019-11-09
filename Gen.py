
def top_ten():

    n = 1

    while n <= 10:
        sq = n * n
        yield sq
        n += 1


value = top_ten()

for i in value:
    print(i)