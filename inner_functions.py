def parent(num):
    print("Printing from parent() function")
    
    
    def first_child():
        print("Priting from the first_child() function")
        
    def second_child():
        print("Priting from the second_child() function")
        
    if num == 1:
        return first_child
    else:
        return second_child
        

    
first = parent(1)
print(first())