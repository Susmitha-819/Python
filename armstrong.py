n=int(input("Enter a number:"))
sum=0
digits=len(str(num))
for i in str(num):
    sum+=int(i)**digits
if sum==num:
    print(num,"is an armstrong number")
else:
    print(num,"is not a armstrong number")
