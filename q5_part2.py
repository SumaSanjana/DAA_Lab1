def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])  
    merged = [intervals[0]]  

    for start, end in intervals[1:]:
        prev_start, prev_end = merged[-1]
        if start <= prev_end: 
            merged[-1] = (prev_start, max(prev_end, end)) 
        else:
            merged.append((start, end))  
    return merged

def main():
    intervals = [(1, 4), (2, 5), (7, 8), (6, 9)]
    non_overlapping_intervals = merge_intervals(intervals)
    print(non_overlapping_intervals)

if __name__ == "__main__":
    main()
