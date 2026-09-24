s = "Python,C;C++|Java,Javascript"
"""Split the string s with different delimiter and join into '-' separator"""
part = []
s = s.split(",")
part.append(s[0])
a = (s[1].split("|"))
part.append(a[1])
b = a[0].split(";")
part.append(b[0])
part.append(b[1])
part.append(s[2])
print(" ".join(part))