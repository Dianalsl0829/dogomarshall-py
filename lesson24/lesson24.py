# Lesson 24
user = True
length = 0
longgest = ''
while user:
    name = input("Enter a name or 'X' to exit: ")
    if name.lower() == "x":
        user  = False
        break
    else:
        if len(name)>length:
            length = len(name)
            longgest = name
print(f"The longgest name is: {longgest}")