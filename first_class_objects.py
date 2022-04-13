# in python function are called first class objects, Functions are like int, string, float which can passed around as arguments

def say_hello(name):
    return f'hello {name}'

def be_awesome(name):
    return f' yo {name} together we are awesome!'

def greet_snowy(func):
    return func("Snowy")


result = greet_snowy(be_awesome) 
# when we call a function without parentheses we acctully call a reference of that function

print(result)