# Lesson 40
def factor(num):
    result =[]
    for i in range(1,num+1):
        if num % i == 0:
            result.append(i)
    return result

def prime(num):
    return len(factor(num)) == 2

def primelist(num):
    primes = [2]
    if num == 2:
        return primes
    else:
        for i in range(3, num, 2):
            if prime(i):
                primes.append(i)

        return primes

# testing
print(f'{primelist(100)}')