lst = [1,2,3,2,4,1,5]

result = []
for num in lst:
    if num not in result:
        result.append(num)

print(result)
