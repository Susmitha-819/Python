n = int(input(1,2,3,5))
nums = list(map(int, input().split()))

for i in range(1, n+1):
    if i not in nums:
        print(i)
        break

