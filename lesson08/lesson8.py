# Lesson 8


w = 0
l = 0
#loop
for i in range(6):
    print("Enter W or L :")
    temp = str(input())
    if temp == "W":
        w += 1
    elif temp!="W" and temp!="L":
        print("Wrong input.")
if w>=5:
    print("Group 1")
elif w >= 3:
    print("Group 2")
elif w >= 1:
    print("Group 3")
else:
    print("Eliminated")