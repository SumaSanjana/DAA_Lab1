import time
import random
import matplotlib.pyplot as plt

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def plot_search_times(size, key):
    arr = generate_random_array(size)
    arr.sort()
    linear_times = []
    binary_times = []

    for _ in range(5):
        start_time = time.time()
        linear_search(arr, key)
        linear_time = time.time() - start_time
        linear_times.append(linear_time)

        start_time = time.time()
        binary_search(arr, key)
        binary_time = time.time() - start_time
        binary_times.append(binary_time)

    plt.plot(range(1, 6), linear_times, label='Linear Search')
    plt.plot(range(1, 6), binary_times, label='Binary Search')
    plt.xlabel('Search Number')
    plt.ylabel('Execution Time (s)')
    plt.title('Time Taken by Linear and Binary Searches for 5 Different Searches')
    plt.legend()
    plt.show()

size = 10000
key = int(input("Enter the search key: "))
plot_search_times(size, key)
