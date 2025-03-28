# Lesson 34
def separating(text):
    '''
    seperats a string argument with a comma then make it to a list
    args:
    text: a string
    return:
    list: a list of integers
    '''
    numlist = text.split(',')
    a_list = []
    for item in numlist:
        a_list.append(int(item))

    return a_list

    # or return[int(item) for item in text.split(',')]
from random import randrange

def randlist(start, end, frequency):
    if start < end and frequency > 0:
        alist =[]
        for an in range(frequency):
            newvalue = randrange(start, end+1)
            alist.append(newvalue)
        return alist
    else:
        return []
    
    #list comprehension method:
    #return [randrange(start, end+1) for an in range(frequency)]




print(separating("2,3,4,5,6,2,1"))
print(randlist(1,1000,10))