import heapq

def find_k_largest_elements(nums, k):
    return heapq.nlargest(k, nums)

def main():
    nums = list(map(int, input("Enter the elements of the array separated by space: ").split()))
    k = int(input("Enter the value of K: "))
    largest_elements = find_k_largest_elements(nums, k)
    print("The", k, "largest elements in the array are:", largest_elements)

if __name__ == "__main__":
    main()
