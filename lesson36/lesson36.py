# Lesson 36
# factors list 
# create a fuction that returns a list of factors of the integer argument

# prime checker
# create a function that returns True if the given nteger argument is a prime number.
def factor(num):
    '''
    creating a list contans all the factor a num have
    arg:
        num: an integer
    return:
        result: a list of num's factor
    '''
    result = []
    if num <= 1:
        result.append(num)
    else:
        for i in range(1, num+1):
            if num % i == 0:
                result.append(i)

    return result

def prime(num):
    '''
    given a number and determin if it is a prime number
    arg:
        num: an interger value
    return:
        boolean
    '''
    # normal way
    if num == 1:
        return False
    elif num<=3:
        return True
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True

    #function in a function way
    if len(factor(num)) != 2:
        return False
    else:
        return True
    
    #or return len(factor(num)) == 2


#testing
print(f'Factor of 13 : {factor(13)}')      
print(f'factor of 36 : {factor(36)}')
print(f'is 13 prime?: {prime(13)}')
print(f'is 36 prime?: {prime(36)}')
