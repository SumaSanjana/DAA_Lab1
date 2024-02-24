import time
import random
A = [random.randint(1, 100) for _ in range(50)]

print("Randomly generated array:", A)
start_time = time.time()

swaps = 0
for i in range(len(A)):
    for j in range(0, len(A)-i-1):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
            swaps += 1

end_time = time.time()
print("Sorted array:")
for i in range(len(A)):
    print("%d" % A[i], end=", ")

print("\nExecution Time: %.8f seconds" % (end_time - start_time))
print("Number of Swaps: %d" % swaps)