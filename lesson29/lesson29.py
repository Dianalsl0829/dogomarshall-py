# Lesson 29
# giving a string, determind the amount of consonants.

# def consonants(text):
#     '''
#     create a value and count for the consonants in the text
#     Args: text: string
#     return: integer as the value of the amount of consonants in the text.
#     '''
#     count  = 0
#     lowcas = text.lower()
#     if not text:
#         return count
#     elif len(text) == 1:
#         if lowcas != "a" and lowcas !="e" and lowcas !="i" and lowcas !="o" and lowcas !="u":
#             count += 1
#         return count
#     else:
#         for i in lowcas:
#             if i != "a" and i !="e" and i !="i" and i !="o" and i !="u":
#                 count += 1
#         return count
# can't makesure it is alphavetical character

def consonants_count(text, vowel = False):
    '''
    rturns the number of consonants in a given string
    Args: 
    text: a string value
    return:
    an interger
    '''
    ctr = 0
    for character in text:
        character = character.lower()
        if character.isalpha() and character not in {'a','e','i','o','u'}:
            ctr += 1

    if not vowel:   
        return ctr
    else:
        vow = 0
        for character in text:
            character = character.lower()
            if character.isalpha() and character in {'a','e','i','o','u'}
            vow += 1
        return vow

word = input()
print(consonants(word))
    