# Lesson 30
# pattern creator
# write a fuction that takes a N integer greater than 0 and output/prints the following pattern.
# N=5
#1
#10
#101
#1010
#10101

def create(num):
    '''
    returns a string of 1 and 0 based on the argument
    args: 
    num: integer, to determin how long the string is 
    return:
    text: series of 1 or 0
    '''
    text = ''

    for i in range (1, num+1):
        if i % 2 == 0:
            text += '0'
        else:
            text += '1'
    
    return text

def output(num):
    '''
    out put all the pattern for each number up to N
    arg:
    num : an integer value
    return:
    no return, print out each pattern
    '''
    for i in range(1, num+1):
        print(create(i))

N = int(input())
print(output(N)) 