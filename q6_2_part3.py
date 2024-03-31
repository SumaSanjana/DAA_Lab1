def two_sum_linear(arr, K):
    arr.sort()
    left = 0
    right = len(arr) - 1

    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == K:
            return True
        elif curr_sum < K:
            left += 1
        else:
            right -= 1

    return False

def main():
    arr = [8, 4, 1, 6]
    K = 10
    result = two_sum_linear(arr, K)
    print("Result:", result)

if __name__ == "__main__":
    main()
