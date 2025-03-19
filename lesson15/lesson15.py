# Lesson 15
condition = True

code = "code"

while condition:
    userinput = input("Enter the code: ")

    if userinput == code:
        print("correct")
        condition = False
    else:
        print("incorrect")


user_input = input("search for a fruit: ")

fruits  = ["apple", "banana", "orange", "grape", "kiwi"]
found  = False

for fruit in fruits:
    if fruit == user_input:
        found = True
        print(f"{user_input} is in the list")

if not found:
    print(f"{user_input} is not in the list")