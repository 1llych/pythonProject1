import random

class Encoder:
    def __init__(self, num):
        self.__num = num

    def __perform_operation(self):
        operation = random.choice([lambda x: x * 2, lambda x: x + 5, lambda x: x - 3])
        return operation(self.__num)

    def __str__(self):
        return str(self.__perform_operation())

e = Encoder(10)
print(e)
