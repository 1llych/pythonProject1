import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Час виконання функції {func.__name__}: {end_time - start_time} секунд")
        return result
    return wrapper
@measure_time
def my_function(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(my_function(10))
