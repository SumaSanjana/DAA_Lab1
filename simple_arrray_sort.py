import random
import time
array1= [random.randint(1, 100) for _ in range(100)]

start_time = time.time()
array1.sort()
end_time = time.time()
print(array1)
print("\nExecution Time: %.8f seconds" % (end_time - start_time))