nums=[1,2,3,4,1,2,3,5]
freq={}
for num in nums:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1

print(freq)        
