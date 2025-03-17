# Lesson 10
telephone =input()
if len(telephone) == 4:
    if (telephone[0] == '8' or telephone[0] == '9') and (telephone[3] == '8' or telephone[3] == '9'):
        if (telephone[1] == telephone[2]):
            print("telemarketer")
        else:
            print("not telemarketer")
    else:
        print("not telemarketer")
else:
    print("wrong number")