# Lesson 39
# determined the GCD greatest common divider
def gcd(num1,num2):
    '''
    find the gcd for num1 and num2
    '''
    divider=[]
    for i in range(1, num1+1):
        if num1 % i == 0 and num2 % i == 0:
            divider.append(i)
    
    return max(divider)

def gcdt(num1,num2):
    for i in range(min(num1,num2),0,-1):
        if num1 % i == 0 and num2 % i == 0:
            return i

#Euclidean Algroithm using Recursion
def e_gcd(num1, num2):
    if num2==0:
        return num1
    else:
        return e_gcd(num2, num1 % num2)

#testing
print(gcd(1080,27))
print(gcdt(1080,27))

