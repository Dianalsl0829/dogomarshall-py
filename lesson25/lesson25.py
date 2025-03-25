# Lesson 25
'''
write a program that can find the prime number factors of a number
1, find all the factors of a number
2, check if the factor is a prime number
3, find the largest prime number
'''
'''
lim = int (input())
maxnum = 0
prime = False
while not prime:
    for num in range(2, lim+1):
        for i in range(2, num):
            print (f"num: {num} i: {i}")
            if num % i == 0:
                break
            else:
                if num > maxnum:
                    maxnum = num
                    print(maxnum)
                else:
                    prime  = True
print(f"the largest prime number is {maxnum}")
'''
# knowing the smallest possible prime factoe is 2.
# continuesly divide the number by 2 
# the next possible prime factor is 3 and odd primes
# set a varialble to 3 and divide the number by 3 as many time as possible until nor divisible
# increment the variable by 2 and repeat the process
# continue to do this until number is 1(num / num ==1)

num = int(input())
numc= num
largest = 0

while num % 2 == 0:
    num //= 2

    largest  = max(largest, 2)

if num != 1:
    factor = 3
    while num != 1:
        if num % factor == 0:
            largest = max(largest, factor)
            num //= factor
        else:
            factor += 2
    pass

print(f'{largest} is the largest prime factor of {numc}')