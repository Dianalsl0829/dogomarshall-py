# Lesson 21
'''
ask N number
find the number that have the most factors
'''
#solution planing
'''
1. ask N number
2. set max_factor = 0, set the result num to 0
3. generate numebr from 1 to N
4. count the number of factors if each number generated
5. if the new count is larger than the max_factor, update the max_factor and the result number
'''

lim = int(input())
most = 0
result  = 0
for i in range(1, lim+1):
    factor = 0
    for j in range(1,i+1):
        if i % j == 0:
            factor +=1 
    if factor > most:
        most = factor
        result = i
print(f'{result} has the most factors in the range from 1 to {lim} with {most} factors.')