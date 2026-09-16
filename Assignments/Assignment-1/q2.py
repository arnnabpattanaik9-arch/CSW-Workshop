x=int(input("Enter your first number :"))
y=int(input("Enter your second number :"))
z=int(input("Enter your third number :"))

if x>=y and x>=z:
    print(f"{x} is greatest")
elif y>=x and y>=z:
    print(f"{y} is greatest")
else :
    print(f"{z} is greatest")