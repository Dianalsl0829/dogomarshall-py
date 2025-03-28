# Lesson 38
#Palindromic Number
def palindrome(text):
    return text == text[::-1]

palindromes =[]
for i in range(999,99,-1):
    for j in range(999,99,-1):
        num = i*j
        if palindrome(str(num)):
            palindromes.append(num)

print(f'the largest palindrome number made from two 3-digit number is {max(palindromes)}')

