from decorators import do_twice, make_pretty

@do_twice
def greet(name):
    print(f"Hello {name}")
    


greet('world')