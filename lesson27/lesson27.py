# Lesson 27
#string cleaning function
# Write a function that removes non-alphabetic characters from the given string. 
# returns it as a lowercase version of the cleand string.

def restring(string):
    '''
    make the string with only alfabetic characters and lower case
    Args:
    string: string
    returns:
    string
    '''
    cleared = ''
    for i in string:
        if i.isalpha():
            cleared += i.lower()
        
    return cleared

user = input("")
print(restring(user))
