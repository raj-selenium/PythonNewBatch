def decorator_func(func):
    def wrapper_func(*args, **kwargs):
        print("**********")
        func(*args,**kwargs)
        print("**********")
    return wrapper_func


@decorator_func
def original_func():
    print("Hi")

@decorator_func
def add(num1, num2):
    print(num1 + num2)

#original_func = decorator_func(original_func)

original_func()
add(10, 3)


def my_timer(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        total_time = time.time()-start_time
        print(f"{func.__name__} executed in {total_time}")
    return wrapper




import time

class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        self.func(*args, **kwargs)
        total_time = time.time() - start_time
        print(f"{self.func.__name__} executed in {total_time}")



@Timer
def loop_func(num):
    for i in range(num):
        time.sleep(0.5)
        print(i)

loop_func(5)