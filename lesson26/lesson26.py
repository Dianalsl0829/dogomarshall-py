# Lesson 26
# function in python
#  Determine the number of factors for each number from 1 to N.
# let N be user input
# def factor_count(number):
#     '''
#     determine the amout of factor it have
#     Args:
#     number: an interger needed
#     Returns:
#     an integer of the number of factors
#     '''
#     counter = 0
#     for i in range(1, number+1):
#         if dividible(number, i):
#             counter +=1
#     return counter

#  def divisible(num1, num2):
#     '''
#     determine if num1 is divisible by num2
#     Args:
#     num1: an integer needed
#     num2: an integer needed
#     Returns:
#     a boolean value
#     '''
#     return num1 % num2 == 0



# lim = int(input())

# for num in range (1, lim+1):
#     size  = factor_count(num)
#     print(f'{num} has {size} factors.')

def divisible(num1, num2):
    '''
    determine if num1 is divisible by num 2
    arg:
    num1 - interger needed
    num2 - interger needed
    return:
    a boolean value
    '''
    return num1 % num2 == 0
def factors(num):
    '''
    find the amout of factors of a number
    arg:
    num: an integer needed
    return:
    an integer of the number's factor.
    '''
    count = 0
    for i in range (1, num+1):
        if divisible(num, i):
            count +=1
    
    return count


lim = int(input())
for num in range(1, lim+1):
    size = factors(num)
    print(f'{num} has {size} factors.')