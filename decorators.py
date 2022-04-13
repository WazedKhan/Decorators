import functools

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
            func(*args, **kwargs)
            return func(*args, **kwargs)
    return wrapper_do_twice

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def good_greeting(func):
    def greeting(*args, **kwargs):
        print(f"Hi, Welcome to Decorators 101. Hope we will get along {args[0]}")
        return func(*args, **kwargs)
    return greeting


def bigest_number(func):
    def find(*args, **kwargs):
        if args[0] > args[1]:
            print(args[0], 'is the max number')
        else:
            print(args[0], 'is the small number')
        return func()
    return find