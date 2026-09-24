decimal = int(input("Enter the decimal number: "))
bint =bin(decimal)[2:]
oint = oct(decimal)[2:]
hint = hex(decimal)[2:]
count = 0
for _ in str(bint):
    count = count + 1
print(f"the binary of {decimal} is {bint}, number of digits is {count}")
count = 0
for _ in str(oint):
    count = count + 1
print(f"the octal of {decimal} is {oint}, number of digits is {count}")
count = 0
for _ in str(hint):
    count = count + 1
print(f"the hexadecimal of {decimal} is {hint}, number of digits is {count}")