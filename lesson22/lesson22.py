# Lesson 22
# fomula : Fib(n) = Fib（n-1) + Fib(n-2)
# Fib(0) = 0, Fib(1) = 1

th = int(input())
 
fib_0 = 0
fib_1 = 1
fib_n = 0

for num in range(2, th+1):
    fib_n = fib_1 + fib_0
    fib_0 = fib_1
    fib_1 = fib_n

prinr (fib_n)