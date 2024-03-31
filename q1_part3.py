def find_pair_with_sum(nums, target):
    num_set = set()

    for num in nums:
        complement = target - num
        if complement in num_set:
            return num, complement
        num_set.add(num)

    return None

def main():
    nums = list(map(int, input("Enter the integers separated by space: ").split()))
    target = int(input("Enter the target sum: "))

    result = find_pair_with_sum(nums, target)
    if result:
        print("Pair found:", result)
    else:
        print("Pair not found.")

if __name__ == "__main__":
    main()
