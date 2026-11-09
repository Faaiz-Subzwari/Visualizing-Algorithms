import random
from BubbleSort.bubbleSort import bubble_sort
from SelectionSort.selectionSort import selection_sort

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
        "Selection Sort" : True
    }

    Validations = {
        "Bubble Sort" : 0,
        "Selection Sort" : 0
    }

    #Validate Bubble Sort
    if Config["Bubble Sort"]:
        for i in range(int(Config["Iterations"])):
            length = random.randint(100,1000)
            print(f'running iteration {i + 1} of Bubble Sort with {length} elements')
            numbers = generate_numbers(length)
            bubble_sort(numbers)
            if validate(numbers):
                Validations["Bubble Sort"] += 1

    #Validate Selection Sort
    if Config["Selection Sort"]:
        for i in range(Config["Iterations"]):
            length = random.randint(100, 1000)
            numbers = generate_numbers(length)
            print(f'running iteration {i + 1} of Selection Sort with {length} elements')
            selection_sort(numbers)
            if validate(numbers):
                Validations["Selection Sort"] += 1

    for key, value in Validations.items():
        print(f'{key} passed {value} out of {Config["Iterations"]} runs')

if __name__ == "__main__":
    main()