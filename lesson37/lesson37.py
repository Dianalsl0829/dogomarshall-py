# Lesson 37
# String compression
def compress(text):
    '''
    compress the string to charcter and number viersion 
    arg:
        text: a string 
    return:
        result: a string
    '''
    result = ''
    counter = 1
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            counter += 1
        else:
            result += text[i-1]
            result += str(counter)
            counter = 1
    result += text[-1] + str(counter)
    
    if len(result)< len(text):
        return result
    else:
        return text


#testing
test = ['aabcccccaaa','abcde','aaabb', 'aabbccddddeeee','a','aaaaaaaaaaabbbbbbbbbb']
for i, testvalue in enumerate(test):
    output = compress(testvalue)
    print(f'test {i+1}')
    print(f'origin {testvalue}')
    print(f'compress version {output}')