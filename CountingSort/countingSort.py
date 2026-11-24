def counting_sort(numbers):
    sorted = [0 for x in range(len(numbers))]
    count = [0 for x in range(max(numbers) + 1)]
    
    for i in range(len(numbers)):
        count[numbers[i]] += 1
        
    for i in range(1, len(count)):
        count[i] += count[i - 1]
        
    for i in range(len(numbers) - 1, -1, -1):
        sorted[count[numbers[i]] - 1] = numbers[i]
        count[numbers[i]] -= 1
        
    return sorted