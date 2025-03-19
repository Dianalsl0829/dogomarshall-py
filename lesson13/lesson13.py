# Lesson 13
#input
month = int(input())
day = int(input())
if month == 2 and day == 18:
    print("This is a specaial day!")
else:
    if month < 2:
        print("Before")
    elif month > 2:
        print("After")
    else:
        if day>18:
            print("After")
        elif day<18:
            print("Before")
