num=int(input("enter a number:"))
sum=0
digits=len(str(num))
for i in str(num):
    sum+=int(i)**digits
if sum==num:
    print("num,is an Aramstrong number")
else:
    print("num,is not an Aramstrong number")
    
        
    
