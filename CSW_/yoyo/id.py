id = input("Enter student's id: ")
if id.isalnum():
    if id[0:3].lower() == "cse":
        if id[3:].isnumeric():
            print(f"integer part of {id} is {id[3:]}")
            print(f"octal decimal of {id[3:]} is {oct(int(id[3:]))}")
            print(f"Student id is {id} and is in valid format")
else:
    print("invalid id format")