def insertion_sort(numbers):
    
    for i in range(len(numbers)):
        smallest = numbers[i]
        for j in range(i, len(numbers)):
            if numbers[j] < smallest:
                smallest = numbers[j]
                numbers[i], numbers[j] = numbers[j], numbers[i]

    return numbers
