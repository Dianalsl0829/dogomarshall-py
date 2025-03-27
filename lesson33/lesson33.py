# Lesson 33
def mean(listnum):
    '''
    calculate the avrage of a list of numbers
    args:
    list: a list that only contains numbers
    return:
    a integer value
    '''
    ave = sum(listnum)/len(listnum)
    return ave
    # // lowers the answer to 个位数


def median(listnum):
    '''
    calculate the middle number of the list
    args:
    listnum: a list that contains numbers
    return:
    a integer value
    '''
    listnum = sorted(listnum)
    mid = len(listnum)//2
    result =0
    if len(listnum) % 2 == 0:
        result = (listnum[mid] + listnum[mid-1]) /2
    else:
        result = listnum[mid]
    return result
    # need to be sorted first

def meant(a_list):


    return sum(a_list)/len(a_list)

def mediant(a_list):
    sortlist = sorted(a_list)
    # sorted()creates a new_list
    # a_list.sort() will mutate a_list  

    middle = len(a_list)//2

    if len(a_list) % 2 == 0:
        left = sortlist[middle-1]
        right = sortlist[middle]
        return (left+right) /2
    else:  
        return sortlist[middle]






#Testing
from random import seed
from random import randrange

seed(1)
data = [randrange(1,100) for i in range(randrange(10,30))]
print (f'Our random dataset is : {data}')
print (f'Our sorted list is : {sorted(data)}')
print(f'Mean of the list is : {mean(data)}')
print(f'Median of the list is : {median(data)}')