s = "PYTHON"
for i in range(len(s)):
    if i%2 == 0:
        print(s[i],"-", sep = "", end = "")
    else:
        if i == len(s) - 1:
            print(s[i], end = "")
        else:
            print(s[i], "*", sep = "", end = "")

word = "PYTHON"
sep = ["-", '*']
part = []
for i,ch in enumerate(word):
    part.append(ch)
    if i < len(word) - 1:
        part.append(sep[i%2])
print("".join(part))