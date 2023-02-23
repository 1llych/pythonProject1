class MyIterable:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self.generator()

    def generator(self):
        for i in range(self.start, self.end):
            yield i

my_iterable = MyIterable(1, 5)
for value in my_iterable:
    print(value)
