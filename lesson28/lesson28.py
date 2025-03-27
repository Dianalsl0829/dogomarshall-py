# Lesson 28
# check if a word is palindrome
# def palindrome(string):
#     '''
#     check if a word is palindrome
#     args: string
#     return: boleen
#     '''
#     if not string:
#         return False #the text is empty string.
#     elif len(string) == 1:
#         return False
#     else:
#         middle = len(string)//2
#         for i in range(0, middle):
#             if string[i] != string[len(string)-1 -i]:
#                 return False
#             else:
#                 return True

def is_palindrome1(text):
    '''
    check if our given argumnt is a palindrome
    args:
    text: an alphavetical based string
    return
    a boolean valuse, true if the text is a palindrome fales otherwise
    '''

    return text  == text[::-1]

def is_palindrome2(text):
    '''
    check if our given argumnt is a palindrome
    args:
    text: an alphavetical based string
    return
    a boolean valuse, true if the text is a palindrome fales otherwise
    '''
    if not text:
        return True
    elif len(text)<4:
        # for string with lengths of 1,2,3
        return text[0] == text[-1]
    else:
        mid  = len(text)//2
        for i in range(0, mid):
            left = text[i]
            rigth = text[-1*i-1]
            if left != right:
                return False # return wroks like a break
        return True

word = input("")
print(is_palindrome1(word), is_palindrome2(word))

