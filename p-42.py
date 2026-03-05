def count_up_to(n):
    count = 1
    while count <=n:
        yield count
        print(count) 
        count +=1
        

counter = count_up_to(5)
list(counter)        
    
