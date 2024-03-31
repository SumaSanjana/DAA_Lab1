import time
import random
import matplotlib.pyplot as plt

def generate_random_numbers(size):
    return [random.randint(1, 10000) for _ in range(size)]

def measure_sorting_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    return time.time() - start_time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def plot_sorting_times(size):
    random_numbers = generate_random_numbers(size)
    bubble_time = measure_sorting_time(bubble_sort, random_numbers.copy())
    selection_time = measure_sorting_time(selection_sort, random_numbers.copy())
    insertion_time = measure_sorting_time(insertion_sort, random_numbers.copy())

    plt.bar(['Bubble Sort', 'Selection Sort', 'Insertion Sort'],
            [bubble_time, selection_time, insertion_time])
    plt.xlabel('Sorting Algorithm')
    plt.ylabel('Time Taken (s)')
    plt.title('Time Taken by Sorting Algorithms')
    plt.show()

def main():
    size = 1000
    plot_sorting_times(size)

if __name__ == "__main__":
    main()
