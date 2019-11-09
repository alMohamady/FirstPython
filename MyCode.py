
class TopTen:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration

ten = TopTen()

print( "From print ", ten.__next__())
print( "From print 2", ten.__next__())
for i in ten:
    print(i)