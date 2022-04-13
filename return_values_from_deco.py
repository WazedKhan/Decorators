from decorators import do_twice

@do_twice
def greeting(name):
    print('Creating Greeting')
    return f'Hi {name}'
    

hi_tintin = greeting('Tintin')
print(hi_tintin)

help(greeting)
greeting.__name__