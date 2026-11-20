def selection_sort(numbers):
    
    for i in range(len(numbers)):
        smallest_idx = i
        for j in range(i, len(numbers)):
            if numbers[j] < numbers[smallest_idx]:
                smallest_idx = j
        numbers[i], numbers[smallest_idx] = numbers[smallest_idx], numbers[i]

    return numbers
