# Lesson 18
# num = int(input())
# ans = []
# for i in range(1, num+1):
#     if num % i == 0 :
#         ans.append(i)
# print(f"The factors of {num} are {ans}")
num = int(input("Enter an integer greater than 0:"))

for divider in range(1, num+1):
    print(f'divider variable is :{divider}')

    if num % divider == 0:
        print(f'{divider} is a factor of {num}.')