def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")



say_hello()    




def count_up_to(n):
    count = 1
    while count <=n:
        yield count
        count +=1
counter = count_up_to(5)
        
    
