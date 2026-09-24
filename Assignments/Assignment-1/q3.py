x=int(input("Enter your first number:"))
y=int(input("Enter your second number:"))
z=input("Select your operator addition(+), substraction(-), multiplication(*),division(/),and modulus(%): ")

if z=="+":
    print(x+y)
elif z=="-":
    print(x-y)
elif z=="*":
    print(x*y)
elif z=="/":
    if y==0:
        print("Divison by 0 is not posiible")
    else:
        print(x/y)
elif z=="%":
    if y==0:
            print("Divison by 0 is not posiible")
    else:
            print(x%y)
else:
    print("Invalid operation")