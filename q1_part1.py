import time
import matplotlib.pyplot as plt

def sum_iterative(N):
    result = 0
    for i in range(1, N+1):
        result += i
    return result

def sum_recursive(N):
    if N == 0:
        return 0
    else:
        return N + sum_recursive(N-1)

def plot_execution_time(max_N):
    N_values = list(range(1, max_N+1))
    iterative_times = []
    recursive_times = []

    for N in N_values:
        start_time = time.time()
        sum_iterative(N)
        iterative_time = time.time() - start_time
        iterative_times.append(iterative_time)

        start_time = time.time()
        sum_recursive(N)
        recursive_time = time.time() - start_time
        recursive_times.append(recursive_time)

    plt.plot(N_values, iterative_times, label='Iterative')
    plt.plot(N_values, recursive_times, label='Recursive')
    plt.xlabel('Value of N')
    plt.ylabel('Execution Time (s)')
    plt.title('Execution Time of Iterative and Recursive Sum Functions')
    plt.legend()
    plt.show()

max_N = int(input("Enter the maximum value of N for testing: "))
plot_execution_time(max_N)
