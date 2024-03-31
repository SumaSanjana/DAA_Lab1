def reverse_string_recursive(s):
    if len(s) <= 1:
        return s
    else:
        return reverse_string_recursive(s[1:]) + s[0]

def main():
    s = input("Enter a string: ")
    reversed_string = reverse_string_recursive(s)
    print("Reversed string:", reversed_string)

if __name__ == "__main__":
    main()
