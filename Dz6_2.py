class Computer:
    def __init__(self, weight, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.weight = weight
        self.years = 40

class Display:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.height = "185cm"
class SmartPhone(Display, Computer):
    def print_info(self):
        print(self.weight)
        print(self.height)
        print(self.years)
iphone = SmartPhone(weight ="70kg")
iphone.print_info()