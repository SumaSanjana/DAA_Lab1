import time
import random
A = [random.randint(1, 100) for _ in range(100)]

print("randommly generated array",A)

start_time = time.time()

swaps = 0
for i in range(len(A)):
    min_idx = i
    for j in range(i + 1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
            swaps += 1

    A[i], A[min_idx] = A[min_idx], A[i]

end_time = time.time()
print("Sorted array:")
for i in range(len(A)):
    print("%d" % A[i], end=", ")

print("\nExecution Time: %.8f seconds" % (end_time - start_time))
print("Number of Swaps: %d" % swaps)