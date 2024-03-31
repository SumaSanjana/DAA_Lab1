def sort_swapped_array(arr):
    first_swap = None
    second_swap = None

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            if first_swap is None:
                first_swap = i
            else:
                second_swap = i + 1
                break

    if second_swap is None:
        return arr  # Array is already sorted

    arr[first_swap], arr[second_swap] = arr[second_swap], arr[first_swap]

    return arr

def main():
    arr = [3, 8, 6, 7, 5, 9]

    sorted_arr = sort_swapped_array(arr)
    print("Sorted array:", sorted_arr)

if __name__ == "__main__":
    main()
