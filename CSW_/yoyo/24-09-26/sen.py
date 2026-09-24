sen = input("Enter the sentence").split()
print(" ".join(sen))
count = 0
for i in " ".join(sen):
    if i.lower() in "aeiou":
        count += 1
print(f"Number of occurence of vowel is {count}")