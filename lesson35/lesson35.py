# Lesson 35
# remove Duplicates
# Creat a function that removes duplicats from the given list argument.

def remove(a_list):

    if len(a_list) <=1:
        return a_list        
    else:
        new = []
        for i in range(0, len(a_list)):
            if a_list[i] not in new:
                new.append(a_list[i])

        return new

#simplist solution to write: conver the arg to set then convert it back to a list

def removet(a_list):
    ''''
    a function that os sed to maintain a single copy of each unique values in a list 
    args:
        a_list: a list of various objects
    return
        new_list : a list containing all unique values
    '''
    new_list = []
    for item in a_list:
        if item not in new_list:
            new_list.append(item)
    return new_list


#test
test = ['a','b','c','c','b','c','a','a','d']
print(f'test list: {test}')
print(f'duplicates removed: {remove(test)}')
print(f'duplicates removed teacher verson: {removet(test)}')

