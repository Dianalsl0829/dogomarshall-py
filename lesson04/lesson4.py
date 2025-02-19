# Lesson 4
# Painting Fences
"""
# method 1
#input
fence1 = input("Enter secition 1:")
fence2 = input("Enter secition 2:")
fence3 = input("Enter secition 3:")
#number of cans you need
totalfence = len(fence1)+len(fence2)+len(fence3)
#cans left over
if(totalfence%12 != 0):
    setcan = (totalfence//12)+1
else:
    setcan = totalfence//12
numcan = setcan*12
mcan = numcan - totalfence
#cost
cost = setcan*14.95

#out put
print(f"{numcan}")
print(f"{mcan}")
print(f"{cost}")
"""
#import
from math import ceil
#input
section1 = input("enter section 1: ")
section2 = input("enter section 2: ")
section3 = input("enter section 3: ")

#process
cans = len(section1)+len(section2)+len(section3)
boxes = ceil(cans/12)#roud up
