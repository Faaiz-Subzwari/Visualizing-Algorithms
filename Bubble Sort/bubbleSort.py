import random
import matplotlib.pyplot as plt
import numpy as np

def generate_numbers(length):
    numbers = [random.randint(0,100) for x in range(length)]
    # numbers = np.array(random.randit(0, 100) for x in range(length))
    return numbers

def sort(numbers):
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - 1 - i):
            if numbers[j + 1] < numbers[j]:
                numbers[j], numbers[j + 1] = numbers[j + 1],  numbers[j]

def validate(numbers):
    for i in range(len(numbers) - 1):
        if(numbers[i + 1] < numbers[i]):
            print('Failed')
    print('Passed')

def plot(numbers):
    fig, ax = plt.subplots()
    ax.plot(numbers)
    plt.show()

def main():
    length = 100    #length of list to generate
    numbers = generate_numbers(length)
    # print("numbers before sorting: ", numbers)
    plot(numbers)
    sort(numbers)
    plot(numbers)
    # print("numbers after sorting: ", numbers)
    validate(numbers)

if __name__ == "__main__":
    main()