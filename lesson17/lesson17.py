# Lesson 17
# num = int(input())
# ans = 1
# if num!=0:
#     for i in range(num,0,-1):
#         ans *= i
# else:
#     ans = 1
# print(ans)

num = int(input())
total = 1
multiplier = 1

while num>=multiplier:
    total *= multiplier
    multiplier +=1
print(total)

