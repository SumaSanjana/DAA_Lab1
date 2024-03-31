def is_palindrome_recursive(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome_recursive(s[1:-1])

def main():
    s = input("Enter a string: ")
    if is_palindrome_recursive(s):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

if __name__ == "__main__":
    main()
