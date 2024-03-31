def two_sum_brute_force(arr, K):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == K:
                return True
    return False

def main():
    arr = [8, 4, 1, 6]
    K = 10
    result = two_sum_brute_force(arr, K)
    print("Result:", result)

if __name__ == "__main__":
    main()
