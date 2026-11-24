import random
from BubbleSort.bubbleSort import bubble_sort
from SelectionSort.selectionSort import selection_sort
from InsertionSort.insertionSort import insertionSort
from CountingSort.countingSort import counting_sort

def generate_numbers(length):
    numbers = [random.randint(0,100) for x in range(length)]
    return numbers

def validate(numbers):
    if numbers == sorted(numbers):
        # print('Passed')
        return True
    # print('Failed')
    return False
        
def main():
    Config = {
        "Iterations" : 10,
        "Bubble Sort" : True,
        "Selection Sort" : True,
        "Insertion Sort" : True,
        "Counting Sort": True
    }

    Validations = {
        "Bubble Sort" : 0,
        "Selection Sort" : 0,
        "Insertion Sort" : 0,
        "Counting Sort" : 0
    }

    #Validate Bubble Sort
    if Config["Bubble Sort"]:
        for i in range(int(Config["Iterations"])):
            length = random.randint(0,1000)
            print(f'running iteration {i + 1} of Bubble Sort with {length} elements')
            numbers = generate_numbers(length)
            bubble_sort(numbers)
            if validate(numbers):
                Validations["Bubble Sort"] += 1

    #Validate Selection Sort
    if Config["Selection Sort"]:
        for i in range(Config["Iterations"]):
            length = random.randint(0, 1000)
            numbers = generate_numbers(length)
            print(f'running iteration {i + 1} of Selection Sort with {length} elements')
            selection_sort(numbers)
            if validate(numbers):
                Validations["Selection Sort"] += 1

    #Validate Insertion Sort
    if Config["Insertion Sort"]:
        for i in range(int(Config["Iterations"])):
            length = random.randint(0, 1000)
            print(f'running iteration {i + 1} of Insertion Sort with {length} elements')
            numbers = generate_numbers(length)
            insertionSort(numbers)
            if validate(numbers):
                Validations["Insertion Sort"] += 1
                
    #Validate Counting Sort
    if Config["Counting Sort"]:
        for i in range(int(Config["Iterations"])):
            length = random.randint(0, 1000)
            print(f'running iteration {i + 1} of Counting Sort with {length} elements')
            numbers = generate_numbers(length)
            new_numbers = counting_sort(numbers)
            if validate(new_numbers):
                Validations["Counting Sort"] += 1

    for key, value in Validations.items():
        print(f'{key} passed {value} out of {Config["Iterations"]} runs')

if __name__ == "__main__":
    main()