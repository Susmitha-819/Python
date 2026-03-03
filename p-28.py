def find_average(arr):
    total = 0
    
    for num in arr:
        total += num
        
    avg = total / len(arr)
    return avg

print(find_average([5, 2, 9, 1, 7]))
