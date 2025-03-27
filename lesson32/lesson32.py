# Lesson 32
def duplicates(text1, text2):
    ''' 
    looking at the characters each string shares
    args:
    text1: a string
    text2: a string
    return:
    list : a lexicographically sorted list of strings
    '''
   
    if not text1 or not text2:
        return []
    else:
        set1 = set(text1)
        set2 =set(text2) # create a set with no dupilicates

        for characters in set1:
            if characters in set2:
                result.apped(characters)
        return sorted(result)

print(duplicates('hello world', 'goodby world'))