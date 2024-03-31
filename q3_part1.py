def string_to_integer_recursive(s):
    if len(s) == 0:
        return 0
    else:
        return int(s[0]) * 10 ** (len(s) - 1) + string_to_integer_recursive(s[1:])

def main():
    s = input("Enter a string of digits: ")
    result = string_to_integer_recursive(s)
    print("Integer representation:", result)

if __name__ == "__main__":
    main()
