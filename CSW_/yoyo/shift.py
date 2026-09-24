def shift_char(c):
    c=chr(ord(c) + 2)
    return c
def main():
    str = input("Enter a word: ")
    print(f"The word {str} after shifting by +2 in unicode is ", end="")
    for i in str:
        print(shift_char(i), end = "")
main()
