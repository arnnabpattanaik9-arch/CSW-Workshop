x=int(input("Enter your age: "))
y=float(input("Enter your percentage: "))
z=float(input("Enter your height: "))
w=float(input("Enter your weight: "))
if x<30 and y>70 and z>5.5 and w<65:
    print("Congratulations! you are selected for the job.")
elif x<30 and 70>y>60 and z>5.5 and w<65:
    print("You are in the waiting list .")
else :
    print("You are rejected.")