# Lesson 19
num = int(input())
# solution 1
'''
the amount of factor should be 2
for loop range fonction count from 1 to number itself
set factor to 0 and add 1 when we find one
after the for loop, if the amount of factor is 2, print prime
'''
counter = 0
for i in range(1, num+1):
    if num % 1 == 0:
        conter+=1

if counter == 2:
    print (f'{num} is a prime number')
else:
    print(f'{num} is a composite number')

# solution 2
'''
assum all number are prime
check numbers from 2 to num-1
if num is divisible by any number, it is not a prime
'''

prime = True
for check in range(2,num):
    if num % check == 0:
        prime = False
        break

if prime:
    print(f'{num} is a prime number')
else:
    print(f'{num} is a composite number')