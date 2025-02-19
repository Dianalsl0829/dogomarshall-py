# Lesson 5
# making cookies

#input
start_money = float(input()) # float() helps to cast its argument to a real number
soled = input()

#initializing variables
# b_cookies = 0
# cookies = 0
b_cookies = soled.count('b')
cookies = soled.count('c')

#counting
for cookie in soled:
    #print(cookie)
    if cookie =='c':
        cookies +=1
    elif cookie =='b':
        b_cookies +=1
    else:
        print("Erro")
#print (b_cookies)
#print(cookies)

#income
amount = b_cookies +cookies
profit = b_cookies*2 + cookies *1.25 - b_cookies*0.75 - cookies*0.25
final_money = start_money + profit
print (f"The amount of cookeis soled is {amount}")
print (f"The profit is ${profit}")
print (f"The total amount of money after selling cookies is ${final_money}")