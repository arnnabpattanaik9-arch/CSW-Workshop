str = input("Enter the string: ")
if len(str) < 7:
    print("doesn't have 7 letters")
else:
    x = str[2:6]
    print(x)
    if x[0] in "AEIOUaeiou":
        print("First character of the extracted substring is a vowel.")
        print(x[::-1])
    else:
        print("First character of the extracted substring is not a vowel.")
        print(x)