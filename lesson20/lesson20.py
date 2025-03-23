# Lesson 20
#solution
'''
set 10000 as the max value
set an answer value
check each number if it is a perfect number
by cheking the sum of it's factor equals to itself
if perfect, add to the asnwer
'''
ans = 0

for num in range(1, 10001):
    tem = 0
    for i in range(1, num):
        if num % i == 0:
            tem += i
        if tem==num:
            ans += num
print(f'the sum of all perfect number is {ans}.')