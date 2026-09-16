x=int(input("Enter your marks: "))

if x>=90 and x<=100:
    print("O grade")
elif x>=80 and x<=89:
    print("A grade")
elif x>=70 and x<=79:
    print("B grade")
elif x>=60 and x<=69:
    print("C grade")
elif x>=50 and x<=59:
    print("D grade")
elif x>=40 and x<=49:
    print("E grade")
else:
    print("Invalid marks")