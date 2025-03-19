# Lesson 16
'''
from 1-50, print the numbers
if the number is a multiple of three: print 'Fizz',
if the number is a multiple of five: print 'Buzz',
if they are multiples of both: print 'FizzBuzz'
otherwise print the number
'''
for num in range(1,51):
    if num%3 == 0 and num%5 == 0:
        print('FizzBuzz')
    elif num%3 == 0:
        print("Fizz")
    elif num%5 == 0:
        print('Buzz')
    else:
        print(num)
