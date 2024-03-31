def segregate_zeros_and_ones(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] == 1:
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1
        else:
            left += 1

    return arr

def main():
    arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]

    segregated_arr = segregate_zeros_and_ones(arr)
    print("Output array:", segregated_arr)

if __name__ == "__main__":
    main()
