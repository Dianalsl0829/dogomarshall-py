# Lesson 11

#input
point  = input()
point = point.split(" ")

''' a long form solution to converting a list with numeric strings to list of integers
fipoint = []
for value in point:
    fipoint.append(int(value))
'''

point = list(map(int, point))

#variable unpacking.
x,y = point
print (f"x is {x}.")
print(f"y is {y}.")

if x>0:
    if y>0:
        print(f"The point of ({x}, {y}) is in quadrant 1.")
    else: 
        print(f"The point of ({x}, {y}) is in quadrant 4.")
else:
    if y>0:
        print(f"The point of ({x}, {y}) is in quadrant 2.")
    else: 
        print(f"The point of ({x}, {y}) is in quadrant 3.")