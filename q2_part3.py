def find_max_product_pair(nums):
    if len(nums) < 2:
        return None

    max_num1 = float('-inf')
    max_num2 = float('-inf')
    min_num1 = float('inf')
    min_num2 = float('inf')

    for num in nums:
        if num > max_num1:
            max_num2 = max_num1
            max_num1 = num
        elif num > max_num2:
            max_num2 = num

        if num < min_num1:
            min_num2 = min_num1
            min_num1 = num
        elif num < min_num2:
            min_num2 = num

    if max_num1 * max_num2 >= min_num1 * min_num2:
        return max_num1, max_num2
    else:
        return min_num1, min_num2

def main():
    nums = list(map(int, input("Enter the integers separated by space: ").split()))

    result = find_max_product_pair(nums)
    if result:
        print("Pair with maximum product:", result)
    else:
        print("No pair found.")

if __name__ == "__main__":
    main()
