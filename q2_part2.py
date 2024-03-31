import heapq

def merge_sorted_lists(sorted_lists):
    merged_list = []
    heap = []

    for i, lst in enumerate(sorted_lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    while heap:
        val, list_idx, element_idx = heapq.heappop(heap)
        merged_list.append(val)
        if element_idx + 1 < len(sorted_lists[list_idx]):
            next_val = sorted_lists[list_idx][element_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, element_idx + 1))

    return merged_list

def main():
    sorted_lists = [
        [10, 20, 30, 40],
        [15, 25, 35],
        [27, 29, 37, 48, 93],
        [32, 33]
    ]
    
    sorted_result = merge_sorted_lists(sorted_lists)
    print(sorted_result)

if __name__ == "__main__":
    main()
