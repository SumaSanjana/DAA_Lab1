def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left_half, left_count = merge_sort(arr[:mid])
    right_half, right_count = merge_sort(arr[mid:])
    sorted_arr, merge_count = merge(left_half, right_half)
    total_count = left_count + right_count + merge_count
    return sorted_arr, total_count

def merge(left, right):
    result = []
    count = 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += len(left) - i
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result, count

def count_inversions(arr):
    _, inversion_count = merge_sort(arr)
    return inversion_count

if __name__ == "__main__":
    input_arr = list(map(int, input("Enter space-separated non-negative integers: ").split()))
    print("Total count of inversions:", count_inversions(input_arr))
