from decorators import good_greeting, bigest_number

@good_greeting
def hello(name):
    print("ok")
    

hello('Wazed')

@bigest_number
def two_number(num1 = 10, num2 = 5):
    print('Here is your result')
    
two_number(10, 5)