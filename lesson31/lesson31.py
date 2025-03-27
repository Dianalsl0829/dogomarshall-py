# Lesson 31
def anagrams(text1, text2):
    '''
    define if two words are anagrams
    args:
    text1: a string
    text2: a other string
    return:
    boolean statement
    '''

    if len(text1) == len (text2):
        text1 = sorted(text1.lower())
        text2 = sorted(text2.lower())
        if text1 == text2:
            return True
        else: 
            return False
    else:
        return False



def anagram(word1,word2):
    '''
    define if the two arguments are anagrams of wach other
    Argument:
        word1: a string 
        word2: a string 
    Return:
        boolean: True if the arguments are anagram, False if not 
    '''
    if len(word1) != len(word2):
        return False
    else:
        for character in word1:
            if word1.count(character) != word2.count(character):
                return False
        return True

def anagram2(word1, word2):
    if len(word1) != len(word2):
        return False
    else:
        list1 = sorted(word1)
        list2 = sorted(word2)
        for i, character in enumerate(list1):
            if list2[i] != character:
                return False
        return True

word1 = input()
word2 = input()
print(anagrams(word1,word2))