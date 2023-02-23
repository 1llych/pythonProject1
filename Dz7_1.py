def calculator(func):
    def wrapper(expression):
        try:
            result = func(expression)
            print("Результат:", result)
        except:
            print("ПОМИЛКА!!!")
    return wrapper
@calculator
def calculate(expression):
    return eval(expression)

calculate("4-5")

