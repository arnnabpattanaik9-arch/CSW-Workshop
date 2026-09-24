list = []
size = int(input("Enter size of list: "))
for _ in range(size):
    y = int(input("Enter the element: "))
    list.append(y)
print("before doubleing" ,list)
for i in range(len(list)):
    list[i] = list[i] * 2
print("After doubling: ", end = '')
print(list)
set = {}